from coffee_machine import CoffeeMachine
from menu import Menu

menu_card = Menu()
menu_card.get_menu()
out_of_machine = False
go_on = True
coffee_machine_object = CoffeeMachine()
while go_on:
    operation = input("Select an operation (monitor, order, exit): ")
    if operation == 'monitor':
        coffee_machine_object.report()
    elif operation == 'order':
        while not out_of_machine:
            ordered_item = input("Choose order (latte, black coffee, cappuccino): ")
            item_resources = menu_card.get_item_from_menu(ordered_item)
            if coffee_machine_object.resources_sufficient(item_resources):
                user_money = coffee_machine_object.enter_money()
                rem_change = coffee_machine_object.calc_change(ordered_item, user_money)
                coffee_machine_object.update_resources(item_resources)
                if rem_change < 0:
                    print("Please enter sufficient amount for your order")
                elif rem_change > 0:
                    print(f"Here is your {ordered_item} ☕\n")
                    print(f"take your remaining change {rem_change}rs")
                    out_of_machine = True
                else:
                    print(f"Here is your {ordered_item} ☕")
                    out_of_machine = True
            else:
                print("Insufficient Resources Available \nConsider owner to refill")
                out_of_machine = True
    elif operation == 'exit':
        print("Thank you!! Visit Again!!!")
        go_on = False
    else:
        print("Please Enter a valid operation")
