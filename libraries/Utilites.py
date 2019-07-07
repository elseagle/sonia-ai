import requests


def get_html(unformatted_url, text):
    search_text = '+'.join(text.split(' '))
    url = unformatted_url.format(search_text)
    r = requests.get(url)
    return r.text
