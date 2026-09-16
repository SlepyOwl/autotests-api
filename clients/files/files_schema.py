from pydantic import BaseModel,HttpUrl

class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str
    

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    file: FileSchema