import pymongo
import certifi

conn_str = "mongodb+srv://admin:admin@cluster0.wfi9o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(conn_str, tlsCAFile=certifi.where())
db = client.get_database("project1")