# db_cnx
# This is the module that handles db connections. Refactor this for your specific db

from pymongo import MongoClient
from bson import ObjectId

class db_connection():
    def __init__(self):
        # Possibly need to refactor to keep the client & database variables private
        try:
            self.client = MongoClient()
        except Exception as e:
            print("Couldn't connect to mongodb. Please make sure mongodb is running, then restart the application. " + e)
        try:
            self.db = self.client.get_database("nnp")
        except Exception as e:
            print("Couldn't connect to npp database. Please restart the application. " + e)
        self.users = self.db.users
        self.inventory = self.db.inventory
        self.orders = self.db.orders

    def db_search_one(self, searchable, collection):
        match collection.lower():
            case "users":
                return self.users.find_one(searchable)
            case "inventory":
                return self.inventory.find_one(searchable)
            case "orders":
                return self.orders.find_one(searchable)
    
    def db_search_many(self,searchable, collection):
        match collection.lower():
            case "users":
                return list(self.users.find(searchable))
            case "inventory":
                return list(self.inventory.find(searchable))
            case "orders":
                return list(self.orders.find(searchable))

    def db_insert(self, insertable, collection):
        match collection.lower():
            case "users":
                return self.users.insert_one(insertable)
            case "inventory":
                return self.inventory.insert_one(insertable)
            case "orders":
                return self.orders.insert_one(insertable)
    
    def db_update(self, searchable, settable, collection):
        match collection.lower():
            case "users":
                return self.users.update_one(searchable, settable)
            case "inventory":
                return self.inventory.update_one(searchable, settable)
            case "orders":
                return self.orders.update_one(searchable, settable)

    def db_delete(self, deleateble, collection):
        match collection.lower():
            case "users":
                return self.users.delete_one(deleateble)
            case "inventory":
                return self.inventory.delete_one(deleateble)
            case "orders":
                return self.orders.delete_one(deleateble)

if __name__ == "__main__":
    my_db_cnx = db_connection()
    selected_item = my_db_cnx.db_search_one({"_id": ObjectId("66997e0eab01322918a5bb8f")}, "inventory")
    my_db_cnx.db_update({"_id": selected_item["_id"]}, {"$inc": {"quantity": (4)}}, "inventory")
    print("The operation has executed! Check MongoDB")