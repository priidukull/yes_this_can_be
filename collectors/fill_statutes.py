from external import statute_crawler
from app.models.statute import Statute

statutes = statute_crawler.StatuteCrawler().fetch_statutes()
result = Statute().insert_many(statutes=statutes)