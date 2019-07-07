from sanic import Sanic

from config.config import config

from controllers.BooksController import BooksController
from controllers.LinksController import LinksController

app = Sanic()

books_controller = BooksController()

app.add_route(books_controller.get_related_books, '/get-books')
app.add_route(LinksController.get_related_links, '/get-links')


if __name__ == '__main__':
    app.run(
        host=config['app']['host'],
        port=config['app']['port']
    )
