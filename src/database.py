from config import DBURL
from pymongo import MongoClient

#client = MongoClient(port=27017)
#db=client.datamad0820


client = MongoClient(DBURL)
db = client.get_database()
