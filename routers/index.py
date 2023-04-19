from fastapi import APIRouter

router = APIRouter()

@router.get('/', tags=['index'])
def index():
    return {'msg': 'Todo API is running'}
