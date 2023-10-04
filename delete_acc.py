import pymongo

def run(client_link,name):
    client = pymongo.MongoClient(client_link)

    db = client['test']

    users = db['accounts']

    cursor = users.count_documents({'name': name})

    if cursor !=0:
        users.update_one({'name' : name}, {'$set' : {'amount' : 0}})
        print(f"Account deleted,\nBalance: {0}")
        dialogue = f"Account deleted,\nBalance: {0}\n"
    else:
        print("Name not Found")
        dialogue = "Name not Found\n"

    client.close()
    return dialogue

#run('mongodb://localhost:27017/','12A45ALENROYTHOMAS')