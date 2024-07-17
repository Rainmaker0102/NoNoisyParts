# biz_dash
# This file is what displays the dashboard for the business management system

class dashboardDisplay():
    def __init__(self, active=True):
        self.DEFAULT_NAME = "Jon Doe"
        self.DEFAULT_PRIVILEGES  = "user"

    def run(self):
        while True:
            print(f"No Noisy Parts! Not Here!")
            print(f"Hello {self.DEFAULT_NAME}! You have {self.DEFAULT_PRIVILEGES} privileges")
            print("What would you like to do today?")
            selection = input("[Q]uit\n[M]ake an Order\n[V]iew past orders\n: ")
            match selection.upper():
                case "Q":
                    print("Exiting the Dashboard")
                    break
                case "M":
                    print("Please code Make Order functionality")
                case "V":
                    print("Please code View Past Order functionality")
                case _:
                    print("That input was not accepted: Input not in input list. Please try again")
            print()


if __name__ == "__main__":
    mainDash = dashboardDisplay()
    mainDash.run()
