from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.data.database import get_db
from app.data.models import Cart
from app.schemas.cart_schemas import CartResponse, CreateCart, UpdateCart, CartResponse

router = APIRouter()

@router.get("/fetch", response_model=list[CartResponse], status_code=status.HTTP_200_OK)
def fetch_carts(db: Session = Depends(get_db)):
    carts = db.query(Cart).all()
    if not carts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The list of carts is empty.")
    return carts

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_cart(cart: CreateCart, db: Session = Depends(get_db)):
    new_cart_item = Cart(user_id=cart.user_id, item_id=cart.item_id, quantity=cart.quantity)
    db.add(new_cart_item)
    db.commit()
    db.refresh(new_cart_item)

@router.put("/update", status_code=status.HTTP_200_OK)
def update_cart(cart: UpdateCart, db: Session = Depends(get_db)):
    target_cart = db.query(Cart).filter(Cart.id == cart.id).first()
    if not target_cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart item not found")

    target_cart.quantity = cart.quantity
    db.commit()
    db.refresh(target_cart)

@router.delete("/delete/{cart_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cart(cart_id: int, db: Session = Depends(get_db)):
    target_cart = db.query(Cart).filter(Cart.id == cart_id).first()
    if not target_cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart item not found")

    db.delete(target_cart)
    db.commit()
     