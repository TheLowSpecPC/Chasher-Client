import pymongo

def run(client_link,name, amount):
    client = pymongo.MongoClient(client_link)

    db = client['test']

    users = db['accounts']

    add = amount
    cursor = users.count_documents({'name' : name})

    if cursor == 0:
        result = users.insert_one({
            'name': name,
            'amount': amount})
        print("New Account Created, Balance: 100")
        dialogue ="New Account Created, Balance: 100\n"
    else:
        find = users.find({'name': name})

        for doc in find:
            add = doc['amount']+add
        users.update_one({'name' : name}, {'$set' : {'amount' : add}})
        print(f"Balance: {add}")
        dialogue = f"Balance: {add}\n"

    client.close()
    return dialogue

#run('mongodb://localhost:27017/','12A45ALENROYTHOMAS',100)