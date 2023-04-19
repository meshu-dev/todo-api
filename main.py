from fastapi import FastAPI
from routers import index, notes

app = FastAPI()

app.include_router(notes.router)
app.include_router(index.router)
