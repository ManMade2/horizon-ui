import avro.schema

_componentResponse = """
{
    "type": "record",
    "name": "ComponentResponse",
    "fields": [
        {
            "name": "html",
            "type": "string"
        }
    ]
}
"""

componentResponse = avro.schema.parse(_componentResponse)

_getButton = """
{
    "type": "record",
    "name": "GetButton",
    "fields": [
        {
            "name": "url",
            "type": "string"
        },
        {
            "name": "id",
            "type": "string"
        },
        {
            "name": "label",
            "type": "string"
        },
        {
            "name": "css_class",
            "type": "string"
        }
    ]
}
"""

getButton = avro.schema.parse(_getButton)


all = [
    _componentResponse.replace("\n", ""),
    _getButton.replace("\n", ""),
]
