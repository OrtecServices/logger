import pymongo


class ConnectionManager(object):

    __client = None
    __database = None
    __collection = None

    def __init__(self, hostname: str, port: str) -> object:
        """MongoClient create a connection
        - default values are : localhost and port 27017"""
        self.__client = pymongo.MongoClient(hostname, port)

    def get_connection(self):
        return self.get_client()

    def get_database(self, databasename):
        self.__database = self.__client.get_database(databasename)
        return self.__database

    def get_collection(self, collection):
        self.__collection = self.__database.get_collection(collection)


if __name__ == '__name__':
    connection_mgr = ConnectionManager("localhost", "27017")
