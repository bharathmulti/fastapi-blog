from fastapi import APIRouter, Depends, HTTPException, status
import schemas, models, database, hashing 
from sqlalchemy.orm import Session
from .repository import user
router = APIRouter(
    prefix='/user',
    tags=['USERS']
)
get_db = database.get_db 



#pwd_cnt = CryptContext(schemes=["bcrypt"], deprecated="auto")
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    #safe_password = request.password[:72] 
    #hashed_password = pwd_cnt.hash(safe_password)
    return user.create_user(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get_user(id, db)




