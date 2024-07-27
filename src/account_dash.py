# Account Dashboard
# This is where a user can update their username or password and delete their account.
# Admins can update any user's username, password, role, or delete them.

# Python Module Imports
from bson import ObjectId

# Project imports
from db_cnx import db_connection
import global_info as gi

class dashboardDisplay():
    def __init__(self, active=True):
        pass

    def update_username(self):
        pass

    def update_password(self):
        pass

    def admin_update_user_username(self):
        pass

    def admin_update_user_password(self):
        pass

    def admin_update_user_role(self):
        pass

    def run(self):
        while True:
            print(f"No Noisy Parts! Not Here!")
            print(f"Hello {gi.current_user["username"]}! You have {gi.current_user["role"]} privileges")
            print("What would you like to do today?")
            selection = input("[Q]uit\nUpdate user[N]ame\nUpdate [P]assword\n: ")
            match selection.upper():
                case "Q":
                    print("Exiting the Dashboard")
                    break
                case "N":
                    print("Please code change username functionality")
                case "P":
                    print("Please code change password functionality")
                case _:
                    print("That input was not accepted: Input not in input list. Please try again")
            print()


if __name__ == "__main__":
    mainDash = dashboardDisplay()
    mainDash.run()
