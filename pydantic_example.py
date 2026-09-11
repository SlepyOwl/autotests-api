from pydantic import BaseModel,Field

class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
 
    is_active: bool = Field(alias="isActive")

user_data ={
    'id' : 1,
    'name': 'Alice',
    'email': 'alice@example.com',
    'isActive': True
}

user = User(
    id=1, 
    name="Anna", 
    email="anna@example.com",
    address=Address(city = "Moscow", zip_code = "1111111")

)
print(user.model_dump())