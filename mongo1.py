import pymongo

client = pymongo.MongoClient("mongodb+srv://name:password@cluster0.wyo7z.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

# SQL - Schema
# name, email, phone, address, city, country

database = client["student"]
collection = database["Student_Info"]


# name, Course1, Course2

ajay = {
    "Name": "Ajay",
    "Course1": "DataScience",
    "Course2":"FullStack"
}

lakshmi = {
    "Name": "Lakshmi",
    "Course1": "DataScience"
}

# collection.insert_one(ajay)
collection.insert_one(lakshmi)
