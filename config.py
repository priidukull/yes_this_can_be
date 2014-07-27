import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

if os.environ.get("MODE") != "test":
    SQLALCHEMY_DATABASE_URI = "postgresql://priidukull:p@localhost:5432/ytcb"
else:
    SQLALCHEMY_DATABASE_URI = "postgresql://priidukull:p@localhost:5432/ytcb_test"

basedir = os.path.abspath(os.path.dirname(__file__))
