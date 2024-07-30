# db_cnx
# This is the module that handles db connections. Refactor this for your specific db

from pymongo import MongoClient
import logging
from time import asctime

class db_connection():
    def __init__(self, parent_module_name="db_cnx"):
        logging.basicConfig(filename=f"nnp-{parent_module_name}-db_log_{asctime()}.log", format=f"{parent_module_name}::%(levelname)s:%(message)s", level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        # Possibly need to refactor to keep the client & database variables private
        try:
            self.logger.info("Connecting to mongodb")
            self.client = MongoClient()
        except Exception as e:
            self.logger.exception("Couldn't connect to mongodb.")
            print("Couldn't connect to mongodb. Please make sure mongodb is running, then restart the application. " + e)
        try:
            self.logger.info("Connection success")
            self.logger.info("Searching for database 'nnp'.")
            self.db = self.client.get_database("nnp")
        except Exception as e:
            self.logger.exception("Couldn't connect to database 'nnp")
            print("Couldn't connect to nnp database. Please restart the application. " + e)
        self.users = self.db.users
        self.inventory = self.db.inventory
        self.orders = self.db.orders

    def db_search_one(self, searchable, collection):
        self.logger.info(f"Searching for one document in collection {collection} with parameter {searchable}")
        match collection.lower():
            case "users":
                return self.users.find_one(searchable)
            case "inventory":
                return self.inventory.find_one(searchable)
            case "orders":
                return self.orders.find_one(searchable)
            case _:
                print("Invalid collection!")
                self.logger.warning(f"A search one operation was tried on a nonexistent collection {collection}")
    
    def db_search_many(self,searchable, collection):
        self.logger.info(f"Searching for many documents in collection {collection} with parameter {searchable}")
        match collection.lower():
            case "users":
                return list(self.users.find(searchable))
            case "inventory":
                return list(self.inventory.find(searchable))
            case "orders":
                return list(self.orders.find(searchable))
            case _:
                print("Invalid collection!")
                self.logger.warning(f"A search many operation was tried on a nonexistent collection {collection}")

    def db_insert(self, insertable, collection):
        self.logger.info(f"Inserting one document {insertable} into collection {collection}")
        match collection.lower():
            case "users":
                return self.users.insert_one(insertable)
            case "inventory":
                return self.inventory.insert_one(insertable)
            case "orders":
                return self.orders.insert_one(insertable)
            case _:
                print("Invalid collection!")
                self.logger.warning(f"An insert operation was tried on a nonexistent collection {collection}")
    
    def db_update(self, searchable, settable, collection):
        self.logger.info(f"Updating one document {searchable} with the parameter {settable} in the collection {collection}")
        match collection.lower():
            case "users":
                return self.users.update_one(searchable, settable)
            case "inventory":
                return self.inventory.update_one(searchable, settable)
            case "orders":
                return self.orders.update_one(searchable, settable)
            case _:
                print("Invalid collection!")
                self.logger.warning(f"An update operation was tried on a nonexistent collection {collection}")

    def db_delete_one(self, deleateble, collection):
        self.logger.info("Deleting one document {deletable} from collection {collection}")
        match collection.lower():
            case "users":
                return self.users.delete_one(deleateble)
            case "inventory":
                return self.inventory.delete_one(deleateble)
            case "orders":
                return self.orders.delete_one(deleateble)
            case _:
                print("Invalid collection!")
                self.logger.warning(f"A delete one operation was tried on a nonexistent collection {collection}")
    
    def db_delete_many(self, deleateble, collection):
        self.logger.info("Deleting many documents following parameter {deletable} in collection {collection}")
        match collection.lower():
            case "users":
                self.users.delete_many(deleateble)
            case "inventory":
                self.inventory.delete_many(deleateble)
            case "orders":
                self.orders.delete_many(deleateble)
            case _:
                print("Invalid collection!")
                self.logger.warning(f"A delete many operation was tried on a nonexistent collection {collection}")

if __name__ == "__main__":
    pass