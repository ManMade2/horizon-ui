# generated by datamodel-codegen:
#   filename:  getAlert.json
#   timestamp: 2024-10-06T08:09:22+00:00

from __future__ import annotations

from pydantic import BaseModel


class GetAlert(BaseModel):
    title: str
    text: str
