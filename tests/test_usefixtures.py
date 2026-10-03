import pytest

@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")

@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаём новые данные в базе данных")


@pytest.mark.usefixtures('clear_books_database', 'fill_books_database')
class TestLibrary:

    def test_read_book_from_library(self, fill_books_database, clear_books_database):
        pass

    def test_delete_book_from_library(self, fill_books_database, clear_books_database):
        pass
    