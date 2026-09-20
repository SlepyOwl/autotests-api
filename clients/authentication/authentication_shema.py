from pydantic import BaseModel,Field,EmailStr
from tools.fakers import fake


class TokenShema(BaseModel):

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refres_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseShema(BaseModel):  

    token: TokenShema


class RefreshRequestShema(BaseModel):

    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)


