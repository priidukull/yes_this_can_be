import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

if os.environ.get("MODE") != "test":
    SQLALCHEMY_DATABASE_URI = "postgresql://priidukull:p@localhost:5432/ytcb"
else:
    SQLALCHEMY_DATABASE_URI = "postgresql://priidukull:p@localhost:5432/ytcb_test"

basedir = os.path.abspath(os.path.dirname(__file__))
