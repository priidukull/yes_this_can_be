#!flask/bin/python-3.4
from app import app
from config import HOST, PORT, DEBUG


app.run(host=HOST, port=PORT, debug=DEBUG)
