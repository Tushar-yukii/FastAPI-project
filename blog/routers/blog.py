from typing import List
from fastapi import APIRouter, Depends, status, HTTPException , Response
from .. import schemas, database , modals
from sqlalchemy.orm import Session
router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)

get_db = database.get_db 
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(get_db)):
    blogs = db.query(modals.Blog).all()
    return blogs


@router.post('/', status_code=status.HTTP_201_CREATED) 
def create(request:schemas.Blog, db : Session = Depends(get_db)): # database instance
    new_blog = modals.Blog(title=request.title, body = request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# delete blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroyed(id , db : Session = Depends(get_db)):
   blog =  db.query(modals.Blog).filter(modals.Blog.id == id)
   if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
   blog.delete(synchronize_session=False)
   db.commit()
   return f'blog id {id} is deleted'
   
# update part  
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db : Session = Depends(get_db)):
   blog = db.query(modals.Blog).filter(modals.Blog.id == id)
   if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
   blog.update(request.model_dump()) # some error
   db.commit()
   return 'updated'
      
# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
# def all(db : Session = Depends(get_db)):
#     blogs = db.query(modals.Blog).all()
#     return blogs

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id , response : Response, db : Session = Depends(get_db)):
    blog = db.query(modals.Blog).filter(modals.Blog.id == id).first()
    if not blog:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                             detail=f"blog with the id {id} not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"blog with the id {id} not available"}
        
    return blog