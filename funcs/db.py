import pymongo


class Db:
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        self.db = client['todo-db']

    def find_all(self, collection_name: str):
        return list(self.db[collection_name].find({}, {'_id': False}))

    def find(self, collection_name:str, query:dict):
        return list(self.db[collection_name].find(query, {'_id': False}))