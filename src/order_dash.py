# Order Dash
# This is where users would Make and View orders and where admin can Update and Delete orders

# Python Module Imports
from bson import ObjectId

# Project imports
from db_cnx import db_connection
import global_info as gi

class dashboardDisplay():
    def __init__(self):
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
            print()
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
                continue
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
                    continue
                print("Restarting the creator")
                continue
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
            selected_item = current_inventory[selection]
            selected_quantity = input("and how many would you like to add to your order? [B]ack: ")
            if selected_quantity == "B":
                print("Restarting the creator")
                continue
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
            order.append({"item_id": selected_item["_id"], "quantity": selected_quantity})

    def admin_update_order(self):
        user_list = self.cnx.db_search_many({}, "users")
        while True:
            print("Please select a user whose orders you'd like to alter")
            for index, user in enumerate(user_list):
                for key, value in user.items():
                    if key == "_id":
                        pass
                    else:
                        print(f"{index}. {key}: {value}")
            user_selection = input("Please select the user whose order you'd like to modify or [Q]uit the menu: ")
            if user_selection.upper() == "Q":
                print("Exiting the menu")
                break
            try:
                user_selection = int(user_selection)
            except ValueError:
                print("Please give valid input of an integer or Q.")
                input("Press enter to continue")
                continue
            if user_selection not in range(len(user_list)):
                print("Your selection was not valid for the list of users. Please review the indexes and make your selection again")
                input("Press enter to continue")
                continue
            selected_user = user_list[user_selection]
            print("Here are the orders for your selected user")
            user_order_list = self.cnx.db_search_many({"user_id": selected_user["_id"]}, "orders")
            for index, order in enumerate(user_order_list):
                for key, value in order.items():
                    if type(value) == list:
                        for item in value:
                            for list_k, list_v in item.items():
                                if list_k == "item_id":
                                    inventory_item_name = self.cnx.db_search_one({"_id": ObjectId(f"{list_v}")}, "inventory")
                                    print(f"{index}. {"Item"}: {inventory_item_name["name"]}")
                                else:
                                    print(f"{index}. {list_k}: {list_v}")
                    else:
                        print(f"{index}. {key}: {value}")
            order_selection = input("Please select the order you'd like to modify or [R]estart the menu: ")
            if order_selection.upper() == "R":
                print("Restarting the menu")
                continue
            try:
                order_selection = int(order_selection)
            except ValueError:
                print("Please give valid input of an integer or R.")
                input("Press enter to continue")
                continue
            if order_selection not in range(len(user_order_list)):
                print("Your selection was not valid for the list of users. Please review the indexes and make your selection again")
                input("Press enter to continue")
                continue
            user_order = user_order_list[order_selection]
            print("Here's the details of that order.")
            for index, item in enumerate(user_order["items"]):
                for key, value in item.items():
                    if key == "item_id":
                        inventory_item_name = self.cnx.db_search_one({"_id": ObjectId(f"{value}")}, "inventory")
                        print(f"{index}. {"Item"}: {inventory_item_name["name"]}")
                    print(f"{index}. {key}: {value}")
            item_selection = input("Please select the item you'd like to modify or [R]estart the menu: ")
            if item_selection.upper() == "R":
                print("Restarting the menu")
                continue
            try:
                item_selection = int(item_selection)
            except ValueError:
                print("Please give valid input of an integer or R.")
                input("Press enter to continue")
                continue
            if item_selection not in range(len(user_order["items"])):
                print("Your selection was not valid for the list of items. Please review the indexes and make your selection again")
                input("Press enter to continue")
                continue
            user_item = user_order["items"][user_selection]
            quantity_selection = input("And what is the new quantity of said item? or [R]estart the menu: ")
            if quantity_selection.upper() == "R":
                print("Restarting the menu")
                continue
            try:
                quantity_selection = int(quantity_selection)
            except ValueError:
                print("Please give valid input of an integer or R.")
                input("Press enter to continue")
                continue
            # NOTE: Usually here would be a check against the current inventory to make sure
            # the quantity given is valid. However, due to this being an admin function
            # we are assuming that the admin is only modifying past orders, and hence
            # a check against the current database would not make sense here
            print("Your operation entails the following")
            print(f"User: {selected_user["username"]}")
            print(f"Order _id: {user_order["_id"]}")
            print(f"Item to modify: {self.cnx.db_search_one({"_id": user_item["item_id"]}, "inventory")["name"]}")
            print(f"New item quantity: {quantity_selection}")
            confirm = input("Would you like to commit this transaction? y/N: ")
            if confirm.upper() == "Y":
                self.cnx.db_update({"_id": user_order["_id"], "items.item_id": user_item["item_id"]}, {"$set": {"items.$.quantity": quantity_selection}}, "orders")
                print("Transaction completed! Restarting the menu")
                continue
            else:
                print("Your transaction has not been committed.")
                continue


    def admin_delete_order(self):
        user_list = self.cnx.db_search_many({}, "users")
        while True:
            print("Here's a list of users in the databse")
            for index, user in enumerate(user_list):
                for key, value in user.items():
                    if key == "_id":
                        pass
                    else:
                        print(f"{index}. {key}: {value}")
            user_selection = input("Please select the user whose order you'd like to delete or [Q]uit the menu: ")
            if user_selection.upper() == "Q":
                print("Exiting the menu")
                break
            try:
                user_selection = int(user_selection)
            except ValueError:
                print("Please give valid input of an integer or Q.")
                input("Press enter to continue")
                continue
            if user_selection not in range(len(user_list)):
                print("Your selection was not valid for the list of users. Please review the indexes and make your selection again")
                input("Press enter to continue")
                continue
            selected_user = user_list[user_selection]
            print("Here are the orders for your selected user")
            user_order_list = self.cnx.db_search_many({"user_id": selected_user["_id"]}, "orders")
            for index, order in enumerate(user_order_list):
                for key, value in order.items():
                    if type(value) == list:
                        for item in value:
                            for list_k, list_v in item.items():
                                if list_k == "item_id":
                                    inventory_item_name = self.cnx.db_search_one({"_id": ObjectId(f"{list_v}")}, "inventory")
                                    print(f"{index}. {"Item"}: {inventory_item_name["name"]}")
                                else:
                                    print(f"{index}. {list_k}: {list_v}")
                    else:
                        print(f"{index}. {key}: {value}")
            order_selection = input("Please select the order you'd like to delete or [R]estart the menu: ")
            if order_selection.upper() == "R":
                print("Restarting the menu")
                continue
            try:
                order_selection = int(order_selection)
            except ValueError:
                print("Please give valid input of an integer or R.")
                input("Press enter to continue")
                continue
            if order_selection not in range(len(user_order_list)):
                print("Your selection was not valid for the list of users. Please review the indexes and make your selection again")
                input("Press enter to continue")
                continue
            user_order = user_order_list[order_selection]
            print("Here's the details of that order.")
            for index, item in enumerate(user_order["items"]):
                for key, value in item.items():
                    print(f"{index}. {key}: {value}")
            print("Your delete operation entails the following")
            print(f"User: {selected_user["username"]}")
            print(f"Order _id: {user_order["_id"]}")
            confirm = input("Would you like to commit this transaction? y/N: ")
            if confirm.upper() == "Y":
                self.cnx.db_delete({"_id": user_order["_id"]}, "orders")
                print("Transaction completed! Restarting the menu")
                continue
            else:
                print("Your transaction has not been committed.")
                continue

    def run(self):
        while True:
            print(f"No Noisy Parts! Not Here!")
            print(f"Hello {gi.current_user["username"]}! You have {gi.current_user["role"]} privileges")
            print("What would you like to do today?")
            if gi.current_user["role"] == "admin":
                ad_menu_confirm = input("You have admin privileges! Would you like to access the admin order menu? y/N: ")
                if ad_menu_confirm.upper() == "Y":
                    selection = input("[Q]uit\n[U]pdate an Order\n[D]elete an order\n: ")
                    match selection.upper():
                        case "Q":
                            print("Exiting the Dashboard")
                            break
                        case "U":
                            self.admin_update_order()
                        case "D":
                            self.admin_delete_order()
                        case _:
                            print("That input was not accepted: Input not in input list. Please try again")
                    print()
                    continue
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
