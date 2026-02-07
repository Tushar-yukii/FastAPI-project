from typing import List
from fastapi import APIRouter, Depends
from .. import schemas, database , modals
from sqlalchemy.orm import Session
router = APIRouter()

@router.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
def all(db : Session = Depends(database.get_db)):
    blogs = db.query(modals.Blog).all()
    return blogs
