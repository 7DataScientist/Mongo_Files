import pymongo

client = pymongo.MongoClient("mongodb+srv://name:password@cluster0.wyo7z.mongodb.net/?retryWrites=true&w=majority")
# db = client.test

database = client['Mongo_Func']
collection = database['Sing_value']

v = {
    "Name":"Winner",
    "Place": "BTM",
    "City":"Bangalore"
}

collection.insert_one(v)


