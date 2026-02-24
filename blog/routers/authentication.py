from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, modals
from sqlalchemy.orm import Session 

router = APIRouter(
    tags=['Authentication']
)
# error
@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(modals.User).filter(
        modals.User.email == request.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )

    return user
