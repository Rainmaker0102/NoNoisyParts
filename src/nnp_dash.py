# Account Dashboard
# This is where a user can update their username or password and delete their account.
# Admins can update any user's username, password, role, or delete them.

# Project imports
import global_info as gi
import account_dash
import inventory_mgmt
import order_dash

class dashboardDisplay():
    def __init__(self):
        pass

    def run(self):
        while True:
            print(f"No Noisy Parts! Not Here!")
            print(f"Hello {gi.current_user["username"]}! You have {gi.current_user["role"]} privileges")
            print("What would you like to do today?")
            if gi.current_user["role"] == "admin":
                selection = input("[Q]uit\n[O]rder dashboard\n[A]ccount dashboard\n[I]nventory management\n: ")
                match selection.upper():
                    case "Q":
                        print("Exiting the Dashboard")
                        break
                    case "O":
                        my_order_dash = order_dash.dashboardDisplay()
                        my_order_dash.run()
                    case "A":
                        my_account_dash = account_dash.dashboardDisplay()
                        my_account_dash.run()
                    case "I":
                        my_inventory_dash = inventory_mgmt.dashboardDisplay()
                        my_inventory_dash.run()
                    case _:
                        print("That input was not accepted: Input not in input list. Please try again")
                print()
                continue
            selection = input("[Q]uit\n[O]rder dashboard\n[A]ccount dashboard\n: ")
            match selection.upper():
                case "Q":
                    print("Exiting the Dashboard")
                    break
                case "O":
                    my_order_dash = order_dash.dashboardDisplay()
                    my_order_dash.run()
                case "A":
                    my_account_dash = account_dash.dashboardDisplay()
                    my_account_dash.run()
                case _:
                    print("That input was not accepted: Input not in input list. Please try again")
            print()


if __name__ == "__main__":
    mainDash = dashboardDisplay()
    mainDash.run()
