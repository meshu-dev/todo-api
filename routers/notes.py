from fastapi import APIRouter, status, HTTPException
from typing import Optional, List
from db.crud import add_note, get_all_notes, get_note, edit_note, delete_note
from db.schema import NewNote, Note, Tag

router = APIRouter(
    prefix="/notes",
    tags=["notes"]
)

@router.post('/', tags=['Post'], response_model=NewNote, status_code=status.HTTP_201_CREATED)
def add_new_note(note: NewNote):
    note = add_note(
        title=note.title,
        text=note.text
    )
    return note

@router.get('/', tags=['Get'], response_model=List[Note], status_code=status.HTTP_200_OK)
def get_note_list():
    notes = get_all_notes()
    return notes

@router.get('/{id}', tags=['Get'], response_model=Note, status_code=status.HTTP_200_OK)
def get_note_by_id(id: int):
    note = get_note(id)

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Todo note doesn\'t exist'
        )

    return note

@router.put('/{id}', tags=['Put'], response_model=Note, status_code=status.HTTP_200_OK)
def edit_note_by_id(id: int, note: Note):
    note = edit_note(
        id=id,
        title=note.title,
        text=note.text,
        is_done=note.is_done
    )
    return note


@router.delete('/{id}', tags=['Delete'], status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_note(id: int):
    note = get_note(id)

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Todo note doesn\'t exist'
        )

    delete_note(id)

    return None
