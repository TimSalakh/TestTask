from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.data.database import get_db
from app.data.models import User
from app.schemas.user_schemas import CreateUser, UpdateUser, UserResponse

router = APIRouter()

@router.get("/fetch", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def fetch_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The list of users is empty.")
    return users

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    new_user = User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def update_user(user_data: UpdateUser, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_data.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    user.name = user_data.name
    db.commit()
    db.refresh(user)

@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    db.delete(user)
    db.commit()
