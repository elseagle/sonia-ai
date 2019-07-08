from .Books import Books
from .StackExchange import StackExchange
from .Utilities import get_html


class Suggestions:

    def __init__(self):
        self.books = Books()

    @staticmethod
    def get_related_links(text):
        html = get_html(StackExchange.links_url, text)
        questions = []
        for text, link in StackExchange.get_links(html):
            questions.append({'text': text, 'link': link})
        return questions

    def get_related_books(self, text):
        books = []
        for title, authors in self.books.get_books(text):
            books.append({'title': title, 'authors': authors})
        return books
