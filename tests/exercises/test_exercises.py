import pytest
from http import HTTPStatus
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_exercise_not_found_response, assert_update_exercise_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(
        self,
        exercises_client:ExercisesClient,
        function_course:CourseFixture
    ):
        request = CreateExerciseRequestSchema(course_id = function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request,response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())    

    def test_get_exercise(
            self,
            exercises_client:ExercisesClient,
            function_exercise:ExerciseFixture
    ):
        request = function_exercise.response.exercise.id
        response = exercises_client.get_exercise_api(request)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_json_schema(response.json(), response_data.model_json_schema()) 

    def  test_update_exercise(
        self,
        exercises_client:ExercisesClient,
        function_exercise:ExerciseFixture
    ):
        update_request = UpdateExerciseRequestSchema()

        request = function_exercise.response.exercise.id
        response = exercises_client.update_exercise_api(request, update_request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)
        
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(update_request,response_data)
        
        validate_json_schema(response.json(), response_data.model_json_schema())

    def  test_delete_exercise (
        self,
        exercises_client:ExercisesClient,
        function_exercise:ExerciseFixture
    ):
        request = function_exercise.response.exercise.id
        response = exercises_client.delete_exercise_api(request)
            
        assert_status_code(response.status_code, HTTPStatus.OK)

        get_request = request
        get_response = exercises_client.get_exercise_api(get_request)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        actual_error = InternalErrorResponseSchema.model_validate_json(get_response.text)
        expected_error = InternalErrorResponseSchema(details="Exercise not found")
        assert_exercise_not_found_response(actual=actual_error, expected=expected_error)