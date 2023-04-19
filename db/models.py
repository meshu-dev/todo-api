from sqlalchemy import create_engine, inspect, MetaData, Table
from sqlalchemy import Column, Date, Integer, String, Boolean, ForeignKey
from sqlalchemy import select, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, declarative_base, sessionmaker, relationship
from db.database import db_init

engine = db_init()

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True)
    notes = relationship('Note', secondary='note_tags', back_populates='tags')

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, unique=True)
    text = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)
    tags = relationship('Tag', secondary='note_tags', back_populates='notes')

class NoteTag(Base):
    __tablename__ = "note_tags"

    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, ForeignKey('notes.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))

Base.metadata.create_all(engine)
