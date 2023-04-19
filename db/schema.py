from pydantic import BaseModel

class NewNote(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True

class Note(BaseModel):
    title: str
    text: str
    is_done: bool

    class Config:
        orm_mode = True

class Tag(BaseModel):
    name: str

    class Config:
        orm_mode = True
