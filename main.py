import pymongo

# Connect to the database
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Connect to the 'test' database
db = client['test']

# Get the 'users' collection
users = db['accounts']

# Find all documents
cursor = users.find({'name': '12A45ALENROYTHOMAS'})

# Iterate over the cursor and print the documents
for doc in cursor:
    print(doc['amount'])

client.close()