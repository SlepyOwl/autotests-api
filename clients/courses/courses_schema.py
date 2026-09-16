from pydantic import BaseModel, ConfigDict, Field

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema



class CourseSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="minScore")
    min_score: int = Field(alias="minScore")
    description: str 
    previewFile: FileSchema 
    estimated_time: str = Field(alias="estimatedTime")
    createdByUser: UserSchema 



class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="minScore")
    min_score: int | None = Field(alias="maxScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")



class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str  = Field(alias="userId")



class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """

    course: CourseSchema