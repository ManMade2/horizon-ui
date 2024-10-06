import fastavro
import json
import os


# Convert Avro types to JSON Schema types
def avro_to_jsonschema_type(avro_type):
    if isinstance(avro_type, list):
        if "null" in avro_type:
            # If 'null' is a valid type, it means the field is optional
            non_null_types = [t for t in avro_type if t != "null"]
            if len(non_null_types) == 1:
                return {"type": avro_to_jsonschema_type(non_null_types[0])}
            return {"type": [avro_to_jsonschema_type(t) for t in non_null_types]}
        else:
            return {"type": [avro_to_jsonschema_type(t) for t in avro_type]}
    elif avro_type == "string":
        return "string"
    elif avro_type == "int":
        return "integer"
    elif avro_type == "long":
        return "integer"
    elif avro_type == "float":
        return "number"
    elif avro_type == "double":
        return "number"
    elif avro_type == "boolean":
        return "boolean"
    elif isinstance(avro_type, dict) and avro_type.get("type") == "record":
        return avro_to_jsonschema(avro_type)
    else:
        raise ValueError(f"Unsupported Avro type: {avro_type}")


# Convert an Avro schema to a JSON Schema
def avro_to_jsonschema(avro_schema):
    jsonschema = {
        "title": avro_schema.get("name", "GeneratedSchema"),
        "type": "object",
        "properties": {},
        "required": [],
    }

    for field in avro_schema["fields"]:
        field_name = field["name"]
        field_type = field["type"]
        jsonschema["properties"][field_name] = {
            "type": avro_to_jsonschema_type(field_type)
        }
        # Check if the field type includes 'null'. If not, it's required.
        if not (isinstance(field_type, list) and "null" in field_type):
            jsonschema["required"].append(field_name)

    if not jsonschema["required"]:
        del jsonschema[
            "required"
        ]  # Remove empty 'required' list if there are no required fields

    return jsonschema


def generate_jsonschema_from_avro(schema_file):
    schema = fastavro.schema.load_schema(schema_file)  # type: ignore
    json_schema = avro_to_jsonschema(schema)

    # Save the JSON schema to a file
    json_schema_file = schema_file.replace(".avsc", ".json")
    file = json_schema_file.split("/")

    with open(f"schemas/json/{file[1]}", "w") as f:
        json.dump(json_schema, f, indent=2)
    print(f"Generated JSON Schema saved to {json_schema_file}")


# Example usage
if __name__ == "__main__":

    root = os.path.dirname(__file__)
    folder = os.path.join(root, "../schemas/")

    allJson = "import avro.schema\n\n"
    names = []

    for fileName in os.listdir(folder):

        if ".avsc" not in fileName:
            continue

        # generate_jsonschema_from_avro(f"schemas/{fileName}")

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
