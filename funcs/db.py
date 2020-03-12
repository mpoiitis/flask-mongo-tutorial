import pymongo


class Db:
    def __init__(self):
        client = pymongo.MongoClient('mongodb+srv://dbUser:dbUserPassword@cluster0-lq1ei.mongodb.net/test?retryWrites=true&w=majority', 27017)
        self.db = client['todo-db']

    def find_all(self, collection_name: str):
        return list(self.db[collection_name].find({}, {'_id': False}))