from fastapi import APIRouter, status, HTTPException
from typing import Optional, List
from db.crud.tag import add_tag, get_all_tags, get_tag, get_tag_by_name, edit_tag, delete_tag
from db.schema import TagData, Tag

router = APIRouter(
    prefix='/tags',
    tags=['tags']
)

@router.post('/', tags=['Post'], response_model=Tag, status_code=status.HTTP_201_CREATED)
def add_new_tag(tag: TagData):
    existing_tag = get_tag_by_name(tag.name)
    
    if existing_tag is not None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='Name is already used for another tag'
        )

    tag = add_tag(
        name=tag.name
    )
    return tag

@router.get('/', tags=['Get'], response_model=List[Tag], status_code=status.HTTP_200_OK)
def get_tag_list():
    tags = get_all_tags()
    return tags

@router.get('/{id}', tags=['Get'], response_model=Tag, status_code=status.HTTP_200_OK)
def get_tag_by_id(id: int):
    tag = get_tag(id)

    if tag is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Todo tag doesn\'t exist'
        )

    return tag

@router.put('/{id}', tags=['Put'], response_model=Tag, status_code=status.HTTP_200_OK)
def edit_tag_by_id(id: int, tag: TagData):
    existing_tag = get_tag_by_name(tag.name)
    
    if existing_tag is not None and existing_tag != id:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='Name is already used for another tag'
        )

    tag = edit_tag(
        id=id,
        name=tag.name
    )
    return tag

@router.delete('/{id}', tags=['Delete'], status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_tag(id: int):
    tag = get_tag(id)

    if tag is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Todo tag doesn\'t exist'
        )

    delete_tag(id)

    return None
