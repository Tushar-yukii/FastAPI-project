from fastapi import FastAPI, Depends
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

@app.post('/blog')
def create(request:schemas.Blog, db : Session = Depends(get_db)):
    new_blog = modals.Blog(title=request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


