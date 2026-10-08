import pytest

@pytest.mark.xfail(reason="Найден баг в приложении из-за которого тест падает с ошибкой")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Баг уже исправлен но на тесте всё ещё висит маркировка xfail")
def test_without_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Внешний сервис временно не доступен")
def test_external_servises_is_unavailable():
    assert 1 == 2