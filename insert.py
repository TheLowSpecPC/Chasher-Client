import pymongo

# Connect to the database
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Connect to the 'test' database
db = client['test']

# Get the 'users' collection
users = db['accounts']

# Insert a single document
if users.find({'name': '12A45ALENROYTHOMAS'}) == None:
    result = users.insert_one({
        'name': '12A45ALENROYTHOMAS',
        'amount': 100
    })
    print(result.inserted_id)

client.close()