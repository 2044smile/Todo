from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o^%y!*!p++5!$w*dz-8i(h24db_y95l6peo4v8a3$=ktp6r-xg'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'admin',
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
            'username': 'admin',
            'password': 'admin',
        }
    }
}
