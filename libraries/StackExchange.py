from bs4 import BeautifulSoup


class StackExchange:

    links_url = 'https://stackexchange.com/search?q={}'

    @staticmethod
    def get_links(html):
        soup = BeautifulSoup(html, 'html.parser')
        results = soup.find_all('div', class_='result-link')
        for result in results:
            text = result.text.strip()
            link = result.find('a').attrs.get('href')
            yield text, link

