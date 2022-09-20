import pymongo

client = pymongo.MongoClient("mongodb+srv://name:password@cluster0.wyo7z.mongodb.net/?retryWrites=true&w=majority")
# db = client.test

database = client['Mongo_Func']
collection = database['Multi_value_1']


lst = [

    {
        "Brand" :"HP",
        "Qty" :100,
        "Config" :{"CPU" :"I5", "Ram" :"8GB", "HD" :"1TB"},
        "W-Class" :"A"
    },

    {
        "Brand": "Dell",
        "Qty": 70,
        "Config": {"CPU": "I5", "Ram": "8GB", "HD": "1TB"},
        "W-Class": "A"
    },

    {
        "Brand": "Lennvo",
        "Qty": 50,
        "Config": {"CPU": "I5", "Ram": "8GB", "HD": "1TB"},
        "W-Class": "B"
    },

    {
        "Brand": "HP",
        "Qty": 50,
        "Config": {"CPU": "I7", "Ram": "16GB", "HD": "1TB"},
        "W-Class": "B"
    },

    {
        "Brand": "Dell",
        "Qty": 125,
        "Config": {"CPU": "I7", "Ram": "16GB", "HD": "1TB"},
        "W-Class": "B"
    },

    {
        "Brand": "Lennvo",
        "Qty": 70,
        "Config": {"CPU": "I7", "Ram": "16GB", "HD": "1TB"},
        "W-Class": "A"
    },

    {
        "Brand": "Acer",
        "Qty": 70,
        "Config": {"CPU": "I7", "Ram": "16GB", "HD": "1TB"},
        "W-Class": "A"
    },

    {
        "Brand": "Acer",
        "Qty": 70,
        "Config": {"CPU": "I5", "Ram": "8GB", "HD": "1TB"},
        "W-Class": "B"
    },

    {
        "Brand": "Lennvo",
        "Qty": 70,
        "Config": {"CPU": "I9", "Ram": "32GB", "HD": "1TB"},
        "W-Class": "C"
    },

    {
        "Brand": "Acer",
        "Qty": 50,
        "Config": {"CPU": "I9", "Ram": "16GB", "HD": "1TB"},
        "W-Class": "C"
    },

]

# collection.insert_many(lst)

# d = collection.find()
# for i in d:
#     print(i)

# e = collection.find({"W-Class":"A"})
#
# for i in e:
#     print(i)

# f = collection.find({"W-Class":{"$in":['A','C']}})
#
# for i in f:
#     print(i)

# g = collection.find({"Brand":{"$gt":"H"}})
#
# for i in g:
#     print(i)

# j = collection.find({"Qty":{"$gt":50}})
#
# for i in j:
#     print(i)

# k = collection.find({"Qty":{"$gte":100}})
#
# for i in k:
#     print(i)


# l = collection.find({"Brand":"Acer1", "Qty":{"$eq":50}})
#
# for i in l:
#     print(i)

# m = collection.find(    {"$or"  :    [   {"Brand":"Acer"}, {"Qty":{"$eq":50}}      ]       }   )
#
# for i in m:
#     print(i)

# n = collection.find( { "$or": [{"Brand":"Acer"} , {'W-Class': 'B'}] })
#
# for i in n:
#     print(i)

# o = collection.update_one({'Brand': 'Acer'}, {"$set":{'Brand': 'Asus'}})

# d = collection.find()
# for i in d:
#     print(i)

# o = collection.update_many({'Brand': 'Acer'}, {"$set":{'Brand': 'Asus'}})
#
# d = collection.find()
# for i in d:
#     print(i)


# p = collection.find({"Config.CPU": "I9"})
#
# for i in p:
#     print(i)
