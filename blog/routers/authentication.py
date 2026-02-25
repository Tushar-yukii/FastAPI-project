from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, modals
from sqlalchemy.orm import Session 
from ..hashing import Hash

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    
    user = db.query(modals.User).filter(
        modals.User.email == request.username
    ).first()

    # PRINTS HERE
    print("Username:", request.username)
    print("User found:", user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
        
        # error
    if not Hash.verify(user.password, request.password):
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect password"
        )

        
    return user

