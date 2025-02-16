from pydantic import BaseModel
from typing import Dict

class User(BaseModel):
    id: str
    name: str

type Users = Dict[str, User]
