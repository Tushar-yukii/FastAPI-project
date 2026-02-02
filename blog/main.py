from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from .import schemas, modals
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
            
modals.Base.metadata.create_all(engine)

@app.post('/blog', status_code=status.HTTP_201_CREATED) 
def create(request:schemas.Blog, db : Session = Depends(get_db)): # database instance
    new_blog = modals.Blog(title=request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# delete blog
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroyed(id , db : Session = Depends(get_db)):
   blog =  db.query(modals.Blog).filter(modals.Blog.id == id)
   if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
   blog.delete(synchronize_session=False)
   db.commit()
   return f'blog id {id} is deleted'
   
# update part  
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db : Session = Depends(get_db)):
   blog = db.query(modals.Blog).filter(modals.Blog.id == id)
   if not blog.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
   blog.update(request.dict()) # some error
   db.commit()
   return 'updated'
      
@app.get('/blog', response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(get_db)):
    blogs = db.query(modals.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id , response : Response, db : Session = Depends(get_db)):
    blog = db.query(modals.Blog).filter(modals.Blog.id == id).first()
    if not blog:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                             detail=f"blog with the id {id} not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"blog with the id {id} not available"}
        
    return blog

@app.post('/user')
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    new_user = modals.User(name = request.name, email = request.email, password = request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)    
    return new_user

