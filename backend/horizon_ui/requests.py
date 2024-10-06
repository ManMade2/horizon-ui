from io import BytesIO

from avro.schema import Schema
from avro.io import DatumReader, BinaryDecoder, DatumWriter, BinaryEncoder
from flask import Response

from horizon_ui.schemas import componentResponse


def deserialize(data: bytes, schema: Schema) -> object:

    data_stream = BytesIO(data)
    decoder = BinaryDecoder(data_stream)
    reader = DatumReader(schema)
    return reader.read(decoder)


def serializeComponent(html: str) -> Response:

    binary_stream = BytesIO()
    writer = DatumWriter(componentResponse)
    encoder = BinaryEncoder(binary_stream)
    writer.write({"html": html}, encoder)
    data = binary_stream.getvalue()

    return Response(data, content_type="application/octet-stream")
