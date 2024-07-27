# Account Creator
# This is where a new user would create an account

# Project imports
import global_info as gi

class dashboardDisplay():
    def __init__(self, active=True):
        pass

    def run(self):
        while True:
            print(f"No Noisy Parts! Not Here!")
            selection = input("Would you like to create an account? Y/n: ")
            match selection.upper():
                case "Y":
                    print("Please code account creator functionality")
                case _:
                    print("Exiting the Dashboard")
                    break
            print()


if __name__ == "__main__":
    mainDash = dashboardDisplay()
    mainDash.run()
