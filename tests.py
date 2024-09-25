import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    @pytest.mark.parametrize('book_name, genre',
    [('Туманность Андромеды', 'Фантастика'),('Аманность Тундромеды', 'Ужасы')])
    def test_set_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('book_name, genre',
    [('Туманность Андромеды', 'Фантастика'), ('Аманность Тундромеды', 'Ужасы')])
    def test_get_book_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('book_name, genre',
    [('Туманность Андромеды', 'Фантастика'), ('Аманность Тундромеды', 'Ужасы')])
    def test_get_books_with_specific_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name in collector.get_books_with_specific_genre(genre)

    def test_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Таня Гроттер')
        collector.set_book_genre('Таня Гроттер', 'Ужасы')
        expected_books_genre = {'Таня Гроттер': 'Ужасы'}
        assert collector.get_books_genre() == expected_books_genre

    @pytest.mark.parametrize('book_name, genre',
    [('Туманность Андромеды', 'Фантастика'), ('Аманность Тундромеды', 'Ужасы')])
    def test_books_for_children(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        if genre in collector.genre_age_rating:
            assert book_name not in collector.get_books_for_children()
        else:
            assert book_name in collector.get_books_for_children()

    @pytest.mark.parametrize("book_name", [
        ('Чевенгур'),
        ('Архипелаг Гулаг'),
    ])
    def test_add_and_delete_book_in_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("День Опричника")
        collector.add_new_book("Колобок")
        collector.add_new_book("Норма")

        collector.add_book_in_favorites("День Опричника")
        collector.add_book_in_favorites("Норма")

        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert "День Опричника" in favorites
        assert "Колобок" not in favorites
        assert "Норма" in favorites
