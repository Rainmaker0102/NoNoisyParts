# Account Dashboard
# This is where a user can update their username or password and delete their account.
# Admins can update any user's username, password, role, or delete them.

# Project imports
from db_cnx import db_connection
import global_info as gi

class dashboardDisplay():
    def __init__(self):
        self.cnx = db_connection("inventory_mgmt")
        self.new_item = {
            "name": "None",
            "price": None,
            "quantity": None
        }
        self.blank_item = {
            "name": "None",
            "price": None,
            "quantity": None
        }

    def add_item(self):
        print("Let's get that new item in the database!")
        while True:
            self.new_item["name"] = input("Please give me the name of the item you'd like to add or [Q]uit: ")
            if self.new_item["name"].upper() == "Q":
                break
            print(f"The item name is {self.new_item["name"]}")
            self.new_item["price"] = input("Please give me the unit price you'd like to give the item or [R]estart: ")
            if self.new_item["price"].upper() == "R":
                continue
            try:
                self.new_item["price"] = float(self.new_item["price"])
            except ValueError:
                print("Please give valid input of a float or R.")
                input("Press enter to continue")
                continue
            print(f"The price for {self.new_item["name"]} is ${self.new_item["price"]} each.")
            self.new_item["quantity"] = input("Please give the initial quantity of the item or [R]estart: ")
            if self.new_item["quantity"].upper() == "R":
                continue
            try:
                self.new_item["quantity"] = int(self.new_item["quantity"])
            except ValueError:
                print("Please give valid input of an integer or R.")
                input("Press enter to continue")
                continue
            print(f"Adding {self.new_item["quantity"]} of the {self.new_item["name"]} at ${self.new_item["price"]} each.")
            confirm = input("Would you like to commit this change? Y/n: ")
            if confirm.upper() not in ("", "Y"):
                self.new_item = self.blank_item
                print("Your item has not been inserted. Restarting.")
                continue
            self.cnx.db_insert(self.new_item, "inventory")
            self.new_item = self.blank_item
            print("Your item has been added to the database!")



    def change_quantity(self):
        print("Let's change the quantity of an item!")
        while True:
            current_inventory = self.cnx.db_search_many({}, "inventory")
            print("Here's a list of available items")
            current_inventory = self.cnx.db_search_many({}, "inventory")
            for index, item in enumerate(current_inventory):
                for key, value in item.items():
                    if key == "_id":
                        pass
                    else:
                        print(f"{index}. {key}: {value}")
            print()
            item_selection = input("Please select an item from the list or [Q]uit: ")
            if item_selection.upper() == "Q":
                break
            try:
                item_selection = int(item_selection)
            except ValueError:
                print("Please give valid input of an integer or Q.")
                input("Press enter to continue")
                continue
            if item_selection not in range(len(current_inventory)):
                print("Your selection was not valid for the inventory. Please review the indexes and make your selection again")
                input("Press enter to continue")
                continue
            selected_item = current_inventory[item_selection]
            print(f"The current quantity of {selected_item["name"]} is {selected_item["quantity"]}")
            new_quantity = input("What's the new quantity? Or [R]estart: ")
            if new_quantity.upper() == "R":
                print("Restarting")
                continue
            try:
                new_quantity = int(new_quantity)
            except ValueError:
                print("Please give valid input of an integer or R.")
                input("Press enter to continue")
                continue
            print(f"Old quantity: {selected_item["quantity"]} and New quantity: {new_quantity}")
            confirm = input("Would you like to commit this change? Y/n: ")
            if confirm.upper() not in ("", "Y"):
                print("Your item's quantity has not been changed. Restarting.")
                continue
            self.cnx.db_update({"_id": selected_item["_id"]}, {"$set": {"quantity": new_quantity}},"inventory")
            print("Your item's quantity has been updated!")

    def change_price(self):
        print("Let's change the price of an item!")
        while True:
            current_inventory = self.cnx.db_search_many({}, "inventory")
            print("Here's a list of available items")
            current_inventory = self.cnx.db_search_many({}, "inventory")
            for index, item in enumerate(current_inventory):
                for key, value in item.items():
                    if key == "_id":
                        pass
                    else:
                        print(f"{index}. {key}: {value}")
            print()
            item_selection = input("Please select an item from the list or [Q]uit: ")
            if item_selection.upper() == "Q":
                break
            try:
                item_selection = int(item_selection)
            except ValueError:
                print("Please give valid input of an integer or Q.")
                input("Press enter to continue")
                continue
            if item_selection not in range(len(current_inventory)):
                print("Your selection was not valid for the inventory. Please review the indexes and make your selection again")
                input("Press enter to continue")
                continue
            selected_item = current_inventory[item_selection]
            print(f"The current price of {selected_item["name"]} is {selected_item["price"]}")
            new_price = input("What's the new price? Or [R]estart: ")
            if new_price.upper() == "R":
                print("Restarting")
                continue
            try:
                new_price = float(new_price)
            except ValueError:
                print("Please give valid input of an float or R.")
                input("Press enter to continue")
                continue
            print(f"Old price: {selected_item["price"]} and New quantity: {new_price}")
            confirm = input("Would you like to commit this change? Y/n: ")
            if confirm.upper() not in ("", "Y"):
                print("Your item's price has not been changed. Restarting.")
                continue
            self.cnx.db_update({"_id": selected_item["_id"]}, {"$set": {"price": new_price}},"inventory")
            print("Your item's price has been updated!")

    def remove_item(self):
        print("Let's remove that item!")
        current_inventory = self.cnx.db_search_many({}, "inventory")
        while True:
            print("Here's a list of available items")
            current_inventory = self.cnx.db_search_many({}, "inventory")
            for index, item in enumerate(current_inventory):
                for key, value in item.items():
                    if key == "_id":
                        pass
                    else:
                        print(f"{index}. {key}: {value}")
            print()
            item_selection = input("Please select an item from the list or [Q]uit: ")
            if item_selection.upper() == "Q":
                break
            try:
                item_selection = int(item_selection)
            except ValueError:
                print("Please give valid input of an integer or Q.")
                input("Press enter to continue")
                continue
            if item_selection not in range(len(current_inventory)):
                print("Your selection was not valid for the inventory. Please review the indexes and make your selection again")
                input("Press enter to continue")
                continue
            selected_item = current_inventory[item_selection]
            print(f"The item marked for deletion is {selected_item["name"]}")
            confirm = input("Would you like to commit this change? Y/n: ")
            if confirm.upper() not in ("", "Y"):
                print("Your item has not been deleted. Restarting.")
                continue
            self.cnx.db_delete_one({"_id": selected_item["_id"]}, "inventory")
            print("Your item has been deleted!")
            

    def run(self):
        while True:
            print(f"Welcome to the Inventory Management Dashboard")
            print(f"Hello {gi.current_user["username"]}! You have {gi.current_user["role"]} privileges")
            print("What would you like to do today?")
            selection = input("[E]xit\n[A]dd item\nChange item [Q]uantity\nChange item [P]rice\n[D]elete an item\n: ")
            match selection.upper():
                case "E":
                    print("Exiting the Dashboard")
                    break
                case "A":
                    self.add_item()
                case "Q":
                    self.change_quantity()
                case "P":
                    self.change_price()
                case "D":
                    self.remove_item()
                case _:
                    print("That input was not accepted: Input not in input list. Please try again")
            print()


if __name__ == "__main__":
    mainDash = dashboardDisplay()
    mainDash.run()
