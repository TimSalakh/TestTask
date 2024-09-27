from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.data.database import get_db
from app.data.models import Item  
from app.schemas.item_schemas import CreateItem, UpdateItem, ItemResponse

router = APIRouter()

@router.get("/fetch", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
def fetch_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    if not items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The list of items is empty.")
    return items

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_item(item: CreateItem, db: Session = Depends(get_db)):
    new_item = Item(name=item.name)  
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

@router.put("/update", status_code=status.HTTP_200_OK)
def update_item(item_data: UpdateItem, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_data.id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    item.name = item_data.name
    db.commit()
    db.refresh(item)

@router.delete("/delete/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    db.delete(item)
    db.commit()