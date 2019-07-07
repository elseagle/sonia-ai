import requests


class Books:

    search_link = 'https://www.googleapis.com/books/v1/volumes?q={}'

    def get_books(self, text):
        url = self.search_link.format(text)
        r = requests.get(url)
        results = r.json()['items']
        for result in results:
            title = result['volumeInfo']['title']
            authors = result['volumeInfo'].get('authors', [])
            yield title, authors
