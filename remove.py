import pymongo

def run(client_link,name, amount):
    client = pymongo.MongoClient(client_link)

    db = client['test']

    users = db['accounts']

    sub = amount

    find = users.find({'name': name})
    cursor = users.count_documents({'name': name})

    if cursor !=0:
        for doc in find:
            sub = doc['amount']-sub
        if sub>=0:
            users.update_one({'name' : name}, {'$set' : {'amount' : sub}})
            print(f"Balance: {sub}")
            dialogue = f"Balance: {sub}\n"
        else:
            print(f"Insuffisant Balance, Balance: {doc['amount']}")
            dialogue = f"Insuffisant Balance, Balance: {doc['amount']}\n"
    else:
        print("Name not Found")
        dialogue = "Name not Found\n"

    client.close()
    return dialogue

#run('mongodb://localhost:27017/','12A45ALENROYTHOMAS',400)