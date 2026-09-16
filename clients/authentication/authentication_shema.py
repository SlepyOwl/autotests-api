from pydantic import BaseModel,Field,EmailStr


class TokenShema(BaseModel):

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refres_token: str = Field(alias="refreshToken")

class LoginRequestShema(BaseModel):

    email: EmailStr
    password: str


class LoginResponseShema(BaseModel):  

    token: TokenShema


class RefreshRequestShema(BaseModel):

    refresh_token: str = Field(alias="refreshToken")


