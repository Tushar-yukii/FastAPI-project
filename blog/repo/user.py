from sqlalchemy.orm import Session
from .. import modals, schemas
from fastapi import HTTPException, status
from ..hashing import Hash


def create(request: schemas.User, db: Session):
    new_user = modals.User(
    name=request.name,
    email=request.email,
    password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
def show(id: int, db: Session):
    user = db.query(modals.User).filter(modals.User.id == id).first()
    if not user:
         raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                             detail=f"user with the id {id} not available")
    return user       