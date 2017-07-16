import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
	'HOST':'127.0.0.1',
	'USER':'alex_root',
	'PASSWORD':'8800',
	'NAME':'students_db',
        #'NAME': os.path.join(BASE_DIR,'..', 'db.sqlite3'),
    }
}