from sqlalchemy.orm import Session
from .. import modals, schemas
from fastapi import HTTPException, status


def get_all(db : Session):
     blogs = db.query(modals.Blog).all()
     return blogs
     
def create(request: schemas.Blog, db: Session):
     new_blog = modals.Blog(title=request.title, body = request.body, user_id=1)
     db.add(new_blog)
     db.commit()
     db.refresh(new_blog)
     return new_blog
        
def destroyed(id: int, db: Session):
    blog =  db.query(modals.Blog).filter(modals.Blog.id == id)
    if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return f'blog id {id} is deleted'

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(modals.Blog).filter(modals.Blog.id == id)
    if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    blog.update(request.model_dump()) # some error
    db.commit()
    return 'updated'

def show(id: int, db: Session):
    blog = db.query(modals.Blog).filter(modals.Blog.id == id).first()
    if not blog:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                             detail=f"blog with the id {id} not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"blog with the id {id} not available"}
    return blog
