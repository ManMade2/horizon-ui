# generated by datamodel-codegen:
#   filename:  getButton.json
#   timestamp: 2024-10-06T07:05:14+00:00

from __future__ import annotations

from pydantic import BaseModel


class GetButton(BaseModel):
    url: str
    id: str
    label: str
    css_class: str
