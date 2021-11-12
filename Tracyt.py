from pymongo import MongoClient
fred="mongodb+srv://tracy:Way2cool@cluster0.jmity.mongodb.net/test?authSource=admin&replicaSet=atlas-7wcfe2-shard-0&readPreference=primary&ssl=truet"
client = MongoClient(fred)

db = client.pytech
print(db.list_collection_names())