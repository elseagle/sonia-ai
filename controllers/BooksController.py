from sanic.response import json

from libraries.Suggestions import Suggestions


class BooksController:

    def __init__(self):
        self.suggestions = Suggestions()

    async def get_related_books(self, request):
        data = request.raw_args
        if not data or 'topic' not in data:
            return json({'message': "Please provide 'topic' as a url param"})
        books = self.suggestions.get_related_books(data['topic'])
        return json(
            {'status': True, 'books': books},
            status=200
        )
