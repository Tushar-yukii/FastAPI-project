from fastapi import APIRouter

from .. repo import schemas

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')

def login(request: schemas.login):
    return 'login'

