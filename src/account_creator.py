# Account Creator
# This is where a new user would create an account

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
        self.new_user = {
            # TECH DEBT: Make an abstraction in the db_cnx for he below operation
            "_id": int(self.cnx.users.find_one(sort=[("_id", -1)])["_id"]) + 1,
            "username": "None",
            "password_hash": "None",
            "role": "user"
        }
        self.blank_user = {
            # TECH DEBT: Make an abstraction in the db_cnx for he below operation
            "_id": int(self.cnx.users.find_one(sort=[("_id", -1)])["_id"]) + 1,
            "username": "None",
            "password_hash": "None",
            "role": "user"
        }

    def set_username(self):
        print("Let's set that username!")
        new_username = input("Please enter the username you would like to use: ")
        confirm = input(f"The username you entered is {new_username}, would you like to commit this change? y/N: ")
        if confirm.upper() == "Y":
            self.new_user["username"] = new_username
            print("Your change has been committed!")
        else:
            print("Your username has not been set.")

    def set_password(self):
        print("Let's set that password!")
        new_password1 = getpass(input("Please enter the username you would like to use: "))
        new_password2 = getpass(input("Confirm your new password"))
        if new_password1 != new_password2:
            print("Your passwords did not match, try again")
            return
        confirm = input(f"Your password has been verified, would you like to commit this change? y/N: ")
        if confirm.upper() == "Y":
            self.new_user["password_hash"] = sha256(new_password1.encode()).hexdigest()
            print("Your change has been committed!")
        else:
            print("Your password has not been modified.")

    def run(self):
        print(f"No Noisy Parts! Not Here!")
        selection = input("Would you like to create an account? Y/n: ")
        match selection.upper():
            case "N":
                print("Exiting the Dashboard")
            case _:
                while True:
                    if self.new_user["username"] == "None":
                        self.set_username()
                    elif self.new_user["password_hash"] == "None":
                        self.set_password()
                    else:
                        confirm = input("Your user credentials have been set. Would you like to create your account? Y/n: ")
                        if confirm.upper() == "N":
                            self.new_user = self.blank_user
                            print("Your account has not been created and the credentials have been reset")
                            quit_confirm = input("Would you like to [Q]uit the account creator? ")
                            if quit_confirm.upper() == "Q":
                                break
                            continue
                        self.cnx.db_insert(self.new_user, "users")
        print()


if __name__ == "__main__":
    mainDash = dashboardDisplay()
    mainDash.run()
