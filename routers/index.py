from fastapi import APIRouter

router = APIRouter()

@router.get('/', tags=['Index'])
def index():
    return {'msg': 'Todo API is running'}
