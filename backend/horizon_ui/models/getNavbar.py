# generated by datamodel-codegen:
#   filename:  getNavbar.json
#   timestamp: 2024-10-06T08:09:22+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Child(BaseModel):
    name: str


class Parent(BaseModel):
    children: List[Child]
