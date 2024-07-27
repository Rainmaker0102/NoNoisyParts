# Order Dash
# This is where users would Make and View orders and where admin can Update and Delete orders

# Python Module Imports
from bson import ObjectId

# Project imports
from db_cnx import db_connection
import global_info as gi

class dashboardDisplay():
    def __init__(self, active=True):
        self.cnx = db_connection()
    
    def view_orders(self):
        search_user_id = gi.current_user["_id"]
        print("Here's a list of your orders")
        order_list = self.cnx.db_search_many({"user_id": search_user_id}, "orders")
        for order in order_list:
            for key, value in order.items():
                if type(value) == list:
                    for item in value:
                        for list_k, list_v in item.items():
                            if list_k == "item_id":
                                inventory_item_name = self.cnx.db_search_one({"_id": ObjectId(f"{list_v}")}, "inventory")
                                print(f"{"Item"}: {inventory_item_name["name"]}")
                            else:
                                print(f"{list_k}: {list_v}")
                else:
                    print(f"{key}: {value}")
        input("Press enter to continue")
    
    def create_order(self):
        print("Let's make that order!")
        order = []
        while True:
            print("What would you like to order?")
            current_inventory = self.cnx.db_search_many({}, "inventory")
            for index, item in enumerate(current_inventory):
                for key, value in item.items():
                    if key == "_id":
                        pass
                    else:
                        print(f"{index}. {key}: {value}")
            print()
            print("Here's your order so far")
            for items in order:
                for key, value in items.items():
                    print(f"{key}: {value}")
            selection = input("Select the number you'd like to add/modify to your order, [R]eset your order, [P]ush your order, or [Q]uit: ")
            if selection.upper() == "Q":
                print("Quitting the creator")
                break
            elif selection.upper() == "R":
                order = []
                print("Your order has been reset!")
                input("Press enter to continue")
            elif selection.upper() == "P":
                confirm_order = input("Are you ready to push your order? y/N: ")
                if confirm_order.upper() == "Y":
                    self.cnx.db_insert({"user_id": gi.current_user["_id"], "items": order}, "orders")
                    for items in order:
                        for key, value in items.items():
                            if key == "item_id":
                                self.cnx.db_update({"_id": value}, {"$inc": {"quantity": -selected_quantity}}, "inventory")
                    order = []
                    print("Your order has been pushed!")
                else:
                    print("Restarting the creator")
                    continue
            else:
                try:
                    selection = int(selection)
                except ValueError:
                    print("Please give valid input of an integer or Q.")
                    input("Press enter to continue")
                    continue
                if selection not in range(len(current_inventory)):
                    print("Your selection was not valid for the inventory. Please review the indexes and make your selection again")
                    input("Press enter to continue")
                    continue
                else:
                    selected_item = current_inventory[selection]
                    selected_quantity = input("and how many would you like to add to your order? [B]ack: ")
                    if selected_quantity == "B":
                        print("Restarting the creator")
                        continue
                    else:
                        try:
                            selected_quantity = int(selected_quantity)
                        except ValueError:
                            print("Please give valid input of an integer or B.")
                            input("Press enter to continue")
                            continue
                        if selected_quantity not in range(selected_item["quantity"]):
                            print("Your selection was not valid for the inventory. Please review the quantity of your selection and make your selection again")
                            input("Press enter to continue")
                            continue
                        else:
                            order.append({"item_id": selected_item["_id"], "quantity": selected_quantity})

    def admin_update_order(self):
        pass

    def admin_delete_order(self):
        pass

    def run(self):
        while True:
            print(f"No Noisy Parts! Not Here!")
            print(f"Hello {gi.current_user["username"]}! You have {gi.current_user["role"]} privileges")
            print("What would you like to do today?")
            selection = input("[Q]uit\n[M]ake an Order\n[V]iew past orders\n: ")
            match selection.upper():
                case "Q":
                    print("Exiting the Dashboard")
                    break
                case "M":
                    self.create_order()
                case "V":
                    self.view_orders()
                case _:
                    print("That input was not accepted: Input not in input list. Please try again")
            print()


if __name__ == "__main__":
    mainDash = dashboardDisplay()
    mainDash.run()
