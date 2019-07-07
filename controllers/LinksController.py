from sanic.response import json

from libraries.Suggestions import Suggestions


class LinksController:

    @staticmethod
    async def get_related_links(request):
        data = request.raw_args
        if not data or 'topic' not in data:
            return json({'message': "Please provide 'topic' as a url param"})
        links = Suggestions.get_related_links(data['topic'])
        return json(
            {'status': True, 'links': links},
            status=200
        )
