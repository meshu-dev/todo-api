from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from db.database import db_init
from db.models import Tag
from datetime import date

Base = declarative_base()

engine = db_init()
session = Session(engine)

def add_tag(name: str):
    tag = Tag(
        name=name
    )
    session.add(tag)
    session.commit()

    return note

def edit_tag(id: int, name: str):
    tag = session.query(Tag).filter_by(id=id).first()
    tag.name = name
    
    session.add(tag)
    session.commit()

    return tag

def get_tag(id):
    tag = session.query(Tag).filter_by(id=id).first()
    return tag

def get_all_tags():
    tags = session.query(Tag).all()
    return tags

def delete_tag(id):
    tag = session.query(Tag).filter_by(id=id).first()

    session.delete(tag)
    session.commit()
