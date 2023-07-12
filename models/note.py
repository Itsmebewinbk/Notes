from pydantic import BaseModel


class Note(BaseModel):
    title: str
    descrtiption: str
    is_main: bool = False
