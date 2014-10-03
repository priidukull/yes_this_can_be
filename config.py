import os

CSRF_ENABLED = True
SECRET_KEY = "Nõmm on sügisele langend kaenlasse."

if os.environ.get("MODE") != "test":
    SQLALCHEMY_DATABASE_URI = "postgresql://priidukull:p@localhost:5432/ytcb"
else:
    SQLALCHEMY_DATABASE_URI = "postgresql://priidukull:p@localhost:5432/ytcb_test"

if os.environ.get("MODE") == "dev":
    HOST = "127.0.0.1"
    PORT = 5000
else:
    HOST = "0.0.0.0"
    PORT = 80

basedir = os.path.abspath(os.path.dirname(__file__))
