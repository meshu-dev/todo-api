from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["index"])
def index():
    return {"msg": "ToDo API is running"}
