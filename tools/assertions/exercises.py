import allure
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("EXERCISE_ASSERTIONS")

@allure.step("Assert exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info(f"Assert exercise")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.order_index, expected.order_index, "order_index")

@allure.step("Assert create exercise response")
def assert_create_exercise_response(request:CreateExerciseRequestSchema, response:CreateExerciseResponseSchema):
    logger.info(f"Assert create exercise response")
    
    
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Assert update exercise response")
def assert_update_exercise_response(actual:UpdateExerciseRequestSchema, expected:UpdateExerciseResponseSchema ):
    logger.info(f"Assert update exercise response")
    
    assert_equal(actual.title, expected.exercise.title, "title")
    assert_equal(actual.max_score, expected.exercise.max_score, "max_score")
    assert_equal(actual.min_score, expected.exercise.min_score, "min_score")
    assert_equal(actual.description, expected.exercise.description, "description")
    assert_equal(actual.estimated_time, expected.exercise.estimated_time, "estimated_time")

@allure.step("Assert exercise not found")
def assert_exercise_not_found_response(actual:InternalErrorResponseSchema, expected:InternalErrorResponseSchema):
    logger.info(f"Assert exercise not found")

    assert_internal_error_response(actual=actual, expected=expected)

@allure.step("Assert get exercise")
def assert_get_exercise_response(
    get_exercise_response: GetExerciseResponseSchema,
    create_exercise_response: CreateExerciseResponseSchema,
):
    """
    Проверяет, что данные упражнения, полученные из ответа API,
    соответствуют данным, полученным при создании упражнения.

    :param get_exercise_response: Ответ API при запросе данных упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если данные упражнения не совпадают.
    """
    logger.info(f"Assert get exercise")

    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

@allure.step("Assert exercises")
def assert_get_exercises_response(
    get_exercise_response: GetExerciseResponseSchema,
    create_exercise_response: list[ExerciseSchema],
):
    """
    Проверяет, что данные упражнения, полученные из ответа API,
    соответствуют данным, полученным при создании упражнения.

    :param get_exercise_response: Ответ API при запросе данных упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если данные упражнения не совпадают.
    """
    logger.info(f"Assert exercises")

    assert_exercise(get_exercise_response.exercises[0], create_exercise_response[0])