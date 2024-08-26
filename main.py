from pymongo import MongoClient

client = MongoClient()
db = client.crud
user_collection = db.users

users = [
    {
        'name': "samyar",
        'password': "123",
        'tell': "09334455345",
        'email': "samyar@mail.com"
    },
    {
        'name': "sarvenaz",
        'password': "123",
        'tell': "09987655656",
        'email': "sarvenaz@mail.com"
    },
    {
        'name': "amirali",
        'password': "123",
        'tell': "09192233443",
        'email': "amirali@mail.com"
    },
    {
        'name': "jila",
        'password': "123",
        'tell': "09876767543",
        'email': "jila@mail.com"
    }
]


def import_first():
    user_collection.insert_many(users)


def update_user():
    myquery = {"name": "jila"}
    newvalues = {"$set": {"name": "ahmad"}}

    user_collection.update_one(myquery, newvalues)


def read_user():
    result = user_collection.find_one({'name': "samyar"})
    print(result)


def delete_user():
    user_collection.delete_one({'name': "sarvenaz"})


if __name__ == '__main__':
    delete_user()
