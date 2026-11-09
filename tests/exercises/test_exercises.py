import pytest
import allure
from http import HTTPStatus
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, GetExerciseResponseSchema, GetExercisesQuerySchema, GetExercisesResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response, assert_update_exercise_response
from tools.assertions.schema import validate_json_schema
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.EXERCISES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.EXERCISES)


class TestExercises:

    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.title("Create exercise")
    @allure.severity(Severity.BLOCKER)

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

    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.title("Get exercise")
    @allure.severity(Severity.BLOCKER)

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

    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.title("Update exercise")
    @allure.severity(Severity.CRITICAL)

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

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    @allure.title("Delete exercise")
    @allure.severity(Severity.CRITICAL)

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

    @allure.tag(AllureTag.GET_ENTITES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    @allure.title("Get exercises")
    @allure.severity(Severity.BLOCKER)

    def test_get_exercises(
        self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture
    ):
        query = GetExercisesQuerySchema(
            courseId=function_exercise.response.exercise.course_id
        )
        response = exercises_client.get_exercises_api(query)
        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_get_exercises_response(response_data, [function_exercise.response.exercise])

        validate_json_schema(response.json(), response_data.model_json_schema())

    