from pydantic import BaseModel

class CreateCart(BaseModel):
    user_id: int
    item_id: int
    quantity: int = 1

class UpdateCart(BaseModel):
    id: int
    quantity: int

class CartResponse(BaseModel):
    id: int
    user_id: int
    item_id: int
    quantity: int

    class Config:
        from_attributes = True
