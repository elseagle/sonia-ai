import os

config = {
    'app': {
        'host': os.getenv('APP_HOST'),
        'port': os.getenv('APP_PORT')
    }
}