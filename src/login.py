# login
# This the page that manages logging in

# Python Imports
from getpass import getpass
from hashlib import sha256

# Project Imports
from db_cnx import db_connection
import global_info as gi
import nnp_dash as nnp
import account_creator as ac

class Login():
    def __init__(self):
        self.connection = db_connection("login")

    def run(self):
        while True:
            print("Please sign in, [M]ake an account, or [Q]uit")
            username = input("Username: ")
            if username.upper() == "Q":
                print("Bye")
                break
            elif username.upper() == "M":
                my_account_creator = ac.dashboardDisplay()
                my_account_creator.run()
                continue
            password = sha256(getpass("Password: ").encode())
            user_search_result = self.connection.db_search_one({"username": username}, "users") or {"username": "None", "password_hash": "None"}
            if user_search_result["username"] != username:
                print("User was not found. Please try again.")
            elif user_search_result["password_hash"] != password.hexdigest():
                print("Password incorrect. Please try again.")
            else:
                gi.current_user = user_search_result
                print(f"Welcome, {username}")
                print("#########################################")
                print()
                my_dash = nnp.dashboardDisplay()
                my_dash.run()


if __name__ == "__main__":
    myLogin = Login()
    myLogin.run()
