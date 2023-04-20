from pydantic import BaseModel

class NewNote(BaseModel):
    title: str
    text: str
    tags: list

    class Config:
        orm_mode = True

class EditNote(BaseModel):
    title: str
    text: str
    is_done: bool

    class Config:
        orm_mode = True

class Note(BaseModel):
    id: int
    title: str
    text: str
    is_done: bool

    class Config:
        orm_mode = True

class TagData(BaseModel):
    name: str

    class Config:
        orm_mode = True

class Tag(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

