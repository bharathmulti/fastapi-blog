from fastapi import APIRouter, Depends, status, Response, HTTPException
import schemas, models, database, hashing
from typing import List
from sqlalchemy.orm import Session 
from .repository import blog
import oauth2
router = APIRouter(
    prefix='/blog',
    tags=['BLOGS']
)

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/', response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlogWithUser)
def show(id: int, response:Response, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f'Blog with the id {id} is not avilable'}
    return blog.show(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED) 
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    
    return blog.update(id, request, db)





