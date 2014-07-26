from db_connection import DbConnection

app = DbConnection().app
app.config.from_object('config')
db = DbConnection().db
engine = DbConnection().engine
conn = DbConnection().conn

from app import views, models

