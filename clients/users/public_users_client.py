from clients.api_client import APIClient

from httpx import Response

from typing import TypedDict


class UserCreateRequest(TypedDict):
    """Структура данных для создания пользователя."""
    email: str 
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для публичных операций с пользователями.
    
    Предназначен для работы с API пользователей без обязательной авторизации.
    Наследуется от абстрактного класса APIClient для обеспечения единообразия структуры API-клиентов.
    
    :param client: экземпляр httpx.Client для выполнения HTTP-запросов
    """
    def __init__(self, client):
        """
        Инициализирует клиент PublicUsersClient.
        
        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """
        super().__init__(client)
    
    def create_user_api():
        """
        """
        super().post('/api/v1/users', UserCreateRequest )
        return Response