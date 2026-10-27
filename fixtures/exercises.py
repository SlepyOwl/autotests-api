from pydantic import BaseModel
import pytest
from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture, function_user

class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(
    exercises_client: ExercisesClient, function_course: CourseFixture
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(courseId=function_course.response.course.id)
    response = exercises_client.create_exercise_api(request)
    return ExerciseFixture(request=request, response=CreateExerciseResponseSchema.model_validate_json(response.text))
