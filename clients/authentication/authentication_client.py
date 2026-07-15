from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

#словарь для логина
class LoginRequestDict(TypedDict):
    email: str
    password: str
#словарь для обновления
class RefreshRequestDict(TypedDict):
    refreshToken: str 

#бла бла
class AuthenticationClient(APIClient):
    
    #Логин
    def login_api(self, request: LoginRequestDict) -> Response :
        return self.post("/api/v1/authentication/login", json=request)
    

    #Обновить
    def refresh_api(self, request: RefreshRequestDict):
        return self.post("/api/v1/authentication/refresh")
    