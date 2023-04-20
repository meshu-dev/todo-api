from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from db.database import db_init
from db.models import Note, Tag
from datetime import date

Base = declarative_base()

engine = db_init()
session = Session(engine)

def add_note(title: str, text: str, is_done: bool = False):
    note = Note(
        title=title,
        text=text,
        is_done=is_done
    )
    session.add(note)
    session.commit()

    return note

def edit_note(id: int, title: str, text: str, is_done: bool = False):
    note = session.query(Note).filter_by(id=id).first()
    note.title = title
    note.text = text
    note.is_done = is_done
    
    session.add(note)
    session.commit()

    return note

def get_note(id):
    note = session.query(Note).filter_by(id=id).first()
    return note

def get_all_notes():
    notes = session.query(Note).all()
    return notes

def delete_note(id):
    note = session.query(Note).filter_by(id=id).first()

    session.delete(note)
    session.commit()
