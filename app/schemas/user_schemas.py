from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

class CreateUser(UserBase):
    pass

class UpdateUser(UserBase):
    id: int

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  
