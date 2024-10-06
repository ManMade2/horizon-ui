import avro.schema

_componentResponse = '''
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
'''

componentResponse = avro.schema.parse(_componentResponse)

_getButton = '''
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
'''

getButton = avro.schema.parse(_getButton)

_getNav = '''
{
    "name": "GetNav",
    "type": "record",
    "fields": [
        {
            "name": "title",
            "type": "string"
        },
        {
            "name": "listItems",
            "type": {
                "type": "array",
                "items": {
                    "name": "listItem",
                    "type": "record",
                    "fields": [
                        {
                            "name": "active",
                            "type": "boolean"
                        },
                        {
                            "name": "url",
                            "type": "string"
                        },
                        {
                            "name": "label",
                            "type": "string"
                        },
                        {
                            "name": "icon",
                            "type": "string"
                        }
                    ]
                }
            }
        }
    ]
}
'''

getNav = avro.schema.parse(_getNav)


all = [
	_componentResponse,
	_getButton,
	_getNav,
]