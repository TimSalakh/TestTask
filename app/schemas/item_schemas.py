from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str

class CreateItem(ItemBase):
    pass

class UpdateItem(ItemBase):
    id: int

class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True  
