import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    machine = SandwichMaker(resources)

    while True:
        choice = input("small/medium/large/report/off: ").lower().strip()

        if choice == "off":
            break
        if choice == "report":
            machine.report()
            continue
        if choice not in recipes:
            print("Invalid option.")
            continue

        item = recipes[choice]
        if machine.check_resources(item["ingredients"]):
            money = machine.process_coins()
            if machine.transaction_result(money, item["cost"]):
                machine.make_sandwich(choice, item["ingredients"])

if __name__=="__main__":
    main()