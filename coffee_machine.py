class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 3000,
            "milk": 2000,
            "coffee": 1000,
        }
        self.money = 0
        self.menu = {
            "latte": {"milk": 50, "water": 100, "coffee": 50, "cost": 20},
            "black coffee": {"milk": 100, "water": 50, "coffee": 150, "cost": 50},
            "cappuccino": {"milk": 150, "water": 50, "coffee": 200, "cost": 100},
        }
    def report(self):
        print(f"water: {self.resources['water']}")
        print(f"water: {self.resources['milk']}")
        print(f"water: {self.resources['coffee']}")

    def update_resources(self, order_item):
        self.resources['water'] -= order_item['water']
        self.resources['coffee'] -= order_item['coffee']
        self.resources['milk'] -= order_item['milk']
        self.money += order_item['cost']

    def resources_sufficient(self, order_item):
        for item in self.resources:
            if self.resources[item] < order_item[item]:
                return False
        return True

    def enter_money(self):
        sum_money = 0
        sum_money += int(input("Enter no.of 50rs coins inserted: "))*50
        sum_money += int(input("Enter no.of 20rs coins inserted: "))*20
        sum_money += int(input("Enter no.of 10rs coins inserted: "))*10
        sum_money += int(input("Enter no.of 5rs coins inserted: "))*5
        return sum_money

    def calc_change(self, item, user_money):
        remain = user_money - self.menu[item]['cost']
        return remain
