from prettytable import PrettyTable
x = PrettyTable(["Item", "cost"])


class Menu:
    def __init__(self):
        self.menu = {
            "latte": {"milk": 50, "water": 100, "coffee": 50, "cost": 20},
            "black coffee": {"milk": 100, "water": 50, "coffee": 150, "cost": 50},
            "cappuccino": {"milk": 150, "water": 50, "coffee": 200, "cost": 100},
        }

    def get_menu(self):
        for item in self.menu:
            x.add_row([item, self.menu[item]['cost']])
        print(x)

    def get_item_from_menu(self, item_name):
        return self.menu[item_name]
