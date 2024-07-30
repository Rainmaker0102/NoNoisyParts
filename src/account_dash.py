# Account Dashboard
# This is where a user can update their username or password and delete their account.
# Admins can update any user's username, password, role, or delete them.

# Python Module Imports
from bson import ObjectId
from hashlib import sha256
from getpass import getpass

# Project imports
from db_cnx import db_connection
import global_info as gi

class dashboardDisplay():
    def __init__(self):
        self.cnx = db_connection()

    def update_username(self):
        print("Let's fix that username!")
        new_username = input("Please enter the new username you would like to use: ")
        confirm = input(f"The username you entered is {new_username}, would you like to commit this change? y/N: ")
        if confirm.upper() == "Y":
            self.cnx.db_update({"_id": gi.current_user["_id"]}, {"$set": {"username": new_username}})
            print("Your change has been committed!")
        else:
            print("Your username has not been modified.")

    def update_password(self):
        print("Let's fix that password!")
        new_password1 = getpass(input("Please enter the username you would like to use: "))
        new_password2 = getpass(input("Confirm your new password"))
        if new_password1 != new_password2:
            print("Your passwords did not match, try again")
            return
        confirm = input(f"Your password has been verified, would you like to commit this change? y/N: ")
        if confirm.upper() == "Y":
            self.cnx.db_update({"_id": gi.current_user["_id"]}, {"$set": {"password_hash": sha256(new_password1.encode()).hexdigest()}})
            print("Your change has been committed!")
        else:
            print("Your password has not been modified.")

    def admin_update_user_username(self):
        user_list = self.cnx.db_search_many({}, "users")
        while True:
            print("Here's a list of users in the databse")
            for index, user in enumerate(user_list):
                for key, value in user.items():
                    if key == "_id":
                        pass
                    else:
                        print(f"{index}. {key}: {value}")
            user_selection = input("Please select the user whose username you'd like to modify or [Q]uit the menu: ")
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
            confirm = input(f"Do you want to update {selected_user["username"]}'s username? Y/n: ")
            if confirm.upper() == "N":
                continue
            new_username = input("Please enter the new username you would like to use: ")
            confirm = input(f"The username you entered is {new_username}, would you like to commit this change? y/N: ")
            if confirm.upper() == "Y":
                self.cnx.db_update({"_id": selected_user["_id"]}, {"$set": {"username": new_username}})
                print("The change has been committed!")
            else:
                print("The username has not been modified.")


    def admin_update_user_password(self):
        user_list = self.cnx.db_search_many({}, "users")
        while True:
            print("Here's a list of users in the databse")
            for index, user in enumerate(user_list):
                for key, value in user.items():
                    if key == "_id":
                        pass
                    else:
                        print(f"{index}. {key}: {value}")
            user_selection = input("Please select the user whose username you'd like to modify or [Q]uit the menu: ")
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
            confirm = input(f"Do you want to update {selected_user["username"]}'s password? Y/n: ")
            if confirm.upper() == "N":
                continue
            print("Let's fix that password!")
            new_password1 = getpass(input("Please enter the username you would like to use: "))
            new_password2 = getpass(input("Confirm your new password"))
            if new_password1 != new_password2:
                print("Your passwords did not match, try again")
                continue
            confirm = input(f"Your password has been verified, would you like to commit this change? y/N: ")
            if confirm.upper() == "Y":
                self.cnx.db_update({"_id": selected_user["_id"]}, {"$set": {"password_hash": sha256(new_password1.encode()).hexdigest()}})
                print("Your change has been committed!")
            else:
                print("Your password has not been modified.")

    def admin_update_user_role(self):
        user_list = self.cnx.db_search_many({}, "users")
        while True:
            print("Here's a list of users in the databse")
            for index, user in enumerate(user_list):
                for key, value in user.items():
                    if key == "_id":
                        pass
                    else:
                        print(f"{index}. {key}: {value}")
            user_selection = input("Please select the user whose username you'd like to modify or [Q]uit the menu: ")
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
            confirm = input(f"Do you want to update {selected_user["username"]}'s username? Y/n: ")
            if confirm.upper() == "N":
                continue
            print(f"The selected user's role is {selected_user["role"]}")
            new_role = input("What is the role you'd like to give to this user? 'user', 'admin', or 'back'")
            if new_role not in ["user", "admin"]:
                print("The user's role hasn't been changed.")
                continue
            self.cnx.db_update({"_id": selected_user["_id"]}, {"$set": {"role": new_role}})
            print(f"The new role has been changed to {new_role}!")
    
    def admin_delete_user(self):
        user_list = self.cnx.db_search_many({}, "users")
        while True:
            print("Here's a list of users in the databse")
            for index, user in enumerate(user_list):
                for key, value in user.items():
                    if key == "_id":
                        pass
                    else:
                        print(f"{index}. {key}: {value}")
            user_selection = input("Please select the user whose username you'd like to modify or [Q]uit the menu: ")
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
            confirm = input(f"Do you want to delete {selected_user["username"]}'s from the database? Y/n: ")
            if confirm.upper() == "N":
                continue
            self.cnx.db_delete_many({"user_id": selected_user["_id"]}, "orders")
            self.cnx.db_delete_one({"_id": selected_user["_id"]})
            print("Deleted user and all orders associated with said user.") 
            

    def run(self):
        while True:
            print(f"No Noisy Parts! Not Here!")
            print(f"Hello {gi.current_user["username"]}! You have {gi.current_user["role"]} privileges")
            print("What would you like to do today?")
            if gi.current_user["role"] == "admin":
                ad_menu_confirm = input("You have admin privileges! Would you like to access the admin order menu? y/N: ")
                if ad_menu_confirm.upper() == "Y":
                    selection = input("[Q]uit\nUpdate user's [U]sername\nUpdate user's [P]assword\nUpdate user's [R]ole\n[D]elete a user\n: ")
                    match selection.upper():
                        case "Q":
                            print("Exiting the Dashboard")
                            break
                        case "U":
                            self.admin_update_user_username()
                        case "P":
                            self.admin_update_user_password()
                        case "R":
                            self.admin_update_user_role()
                        case "D":
                            self.admin_delete_user()
                        case _:
                            print("That input was not accepted: Input not in input list. Please try again")
                    print()
                    continue
            selection = input("[Q]uit\nUpdate user[N]ame\nUpdate [P]assword\n: ")
            match selection.upper():
                case "Q":
                    print("Exiting the Dashboard")
                    break
                case "N":
                    self.update_username()
                case "P":
                    self.update_password()
                case _:
                    print("That input was not accepted: Input not in input list. Please try again")
            print()


if __name__ == "__main__":
    mainDash = dashboardDisplay()
    mainDash.run()
