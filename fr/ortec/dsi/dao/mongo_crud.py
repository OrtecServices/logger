from fr.ortec.dsi.dao.ConnectionManager import ConnectionManager


class MongoDao(object):

    __database = None
    __connection = None

    def __init__(self, database):
        connection = ConnectionManager("localhost", "27017")
        self.__database = connection.get_database(database)

    def create(self, collection, json_data):
        coll = self.__database.get_collection(collection)
        result = coll.insert_one(json_data)
        print(result.inserted_id)

    def update(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError


if __name__ == '__main__':
    mongo_dao = MongoDao("logs")
