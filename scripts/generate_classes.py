import fastavro
import json
import os


def avro_type_to_openapi_type(avro_type):
    """Maps Avro primitive types to OpenAPI types."""
    if isinstance(avro_type, list):
        # Handle unions (e.g., ['null', 'string'])
        avro_type = [t for t in avro_type if t != "null"][0]

    avro_to_openapi_map = {
        "string": {"type": "string"},
        "boolean": {"type": "boolean"},
        "int": {"type": "integer", "format": "int32"},
        "long": {"type": "integer", "format": "int64"},
        "float": {"type": "number", "format": "float"},
        "double": {"type": "number", "format": "double"},
        "bytes": {"type": "string", "format": "binary"},
    }

    if isinstance(avro_type, dict) and avro_type["type"] == "array":
        return {"type": "array", "items": avro_type_to_openapi_type(avro_type["items"])}

    if isinstance(avro_type, dict) and avro_type["type"] == "record":
        return avro_record_to_openapi(avro_type)

    if isinstance(avro_type, dict) and avro_type["type"] == "enum":
        return {"type": "string", "enum": avro_type["symbols"]}

    return avro_to_openapi_map.get(avro_type, {"type": "object"})  # type: ignore


def avro_record_to_openapi(record):
    """Converts an Avro record (complex type) to OpenAPI."""
    properties = {}
    required = []

    for field in record["fields"]:
        properties[field["name"]] = avro_type_to_openapi_type(field["type"])
        if "default" not in field:
            required.append(field["name"])

    return {
        "type": "object",
        "properties": properties,
        "required": required if required else None,
    }


def avro_to_openapi(schema):
    """Converts an Avro schema to OpenAPI 3.0."""
    openapi_schema = {
        "openapi": "3.0.0",
        "info": {"title": "API Schema", "version": "1.0.0"},
        "paths": {},
        "components": {"schemas": {schema["name"]: avro_record_to_openapi(schema)}},
    }

    return openapi_schema


# Example usage
if __name__ == "__main__":

    root = os.path.dirname(__file__)
    folder = os.path.join(root, "../schemas/")

    allJson = "import avro.schema\n\n"
    names = []

    for fileName in os.listdir(folder):

        if ".avsc" not in fileName:
            continue

        with open(f"schemas/{fileName}", "r") as f:
            avro_schema = json.load(f)

        openapi_schema = avro_to_openapi(avro_schema)
        with open(f"schemas/json/{fileName.removesuffix(".avsc")}.json", "w") as f:
            json.dump(openapi_schema, f, indent=2)

        with open(f"schemas/{fileName}", "r") as f:
            name = fileName.removesuffix(".avsc")
            names.append(name)
            allJson += f"_{name} = '''\n{f.read()}\n'''\n\n"
            allJson += f"{name} = avro.schema.parse(_{name})\n\n"

    x = os.path.join(root, "../backend/horizon_ui/schemas.py")
    allJson += f"\nall = [\n"

    for name in names:
        allJson += f"\t_{name},\n"

    allJson += "]"

    with open(x, "w") as f:
        f.write(allJson)
