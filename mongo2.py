import pymongo

client = pymongo.MongoClient("mongodb+srv://name:password@cluster0.wyo7z.mongodb.net/?retryWrites=true&w=majority")

database = client["Gen_JSON"]
collection = database["Tab_JSON"]

d = {'success': {'total': 1}, 'contents': {'quotes': [{'quote': 'The man who removes a mountain begins by carrying away small stones..', 'length': '71', 'author': 'Chinese Proverb', 'tags': ['inspire', 'moving-mountains'], 'category': 'inspire', 'language': 'en', 'date': '2022-08-26', 'permalink': 'https://theysaidso.com/quote/chinese-proverb-the-man-who-removes-a-mountain-begins-by-carrying-away-small-sto', 'id': 'h7Gyu282q_vzBWvn2zdmtweF', 'background': 'https://theysaidso.com/img/qod/qod-inspire.jpg', 'title': 'Inspiring Quote of the day'}]}, 'baseurl': 'https://theysaidso.com', 'copyright': {'year': 2024, 'url': 'https://theysaidso.com'}}

collection.insert_one(d)
