class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollar_coins = int(input("How many large dollars coins? "))
        half_dollar_coins = int(input("How many half dollar coins? "))
        quarter_coins = int(input("How many quarters? "))
        nickle_coins = int(input("How many nickles? "))

        coins = (dollar_coins * 1) + (half_dollar_coins * .5) + (quarter_coins * .25) + (nickle_coins * .05)
        return coins

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry that's not enough money. Money Refunded.")
            return False
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
        return True