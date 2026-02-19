import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():

    while True:
        choice = input("small/medium/large/report/off: ").lower().strip()

        if choice == "off":
            break
        if choice == "report":
            sandwich_maker_instance.report()
            continue
        if choice not in recipes:
            print("Invalid option.")
            continue

        item = recipes[choice]
        if sandwich_maker_instance.check_resources(item["ingredients"]):
            money = cashier_instance.process_coins()
            if cashier_instance.transaction_result(money, item["cost"]):
                sandwich_maker_instance.make_sandwich(choice, item["ingredients"])

if __name__=="__main__":
    main()