from fastapi import FastAPI
from routers import index, notes, tags

app = FastAPI()

app.include_router(index.router)
app.include_router(notes.router)
app.include_router(tags.router)
