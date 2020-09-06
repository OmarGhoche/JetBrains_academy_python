# Write your code here
'''
------------------------- STAGE #1 ---------------------------
coffee_message = ("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")

def print_it(string, split):
    to_split = string.split("split")
    for i in to_split:
        print(i)

print_it(coffee_message, "\n")

--------------------------STAGE #2 --------------------------------------------

print("Write how many cups of coffee you will need:")
cups_of_coffee = int(input("> "))

print(f"For {cups_of_coffee} cups of coffee you will need:")
print(f"{cups_of_coffee * 200} ml of water")  # 200ml water per cup
print(f"{cups_of_coffee * 50} ml of milk")  # 50ml milk per cup
print(f"{cups_of_coffee * 15} g of coffee beans")  # 15g per cup


# -------------------- STAGE #3 --------------------------

print("Write how many ml of water the coffee machine has:")
a_water = int(input("> "))  # 200ml water per cup // *a_ stands for `amount`
# max cups based in amount of WATER
n_water = a_water // 200 #  ml // *n_ stands for `number`

print("Write how many ml of milk the coffee machine has:")
a_milk = int(input("> "))  # 50ml milk per cup // *a_ stands for `amount`
# max cups based in amount of MILK
n_milk = a_milk // 50 #  ml // *n_ stands for `number`

print("Write how many grams of coffee beans the coffee machine has:")
a_coffee = int(input("> "))  # 15g per cup // *a_ stands for `amount`
# max cups based in amount of COFFEE BEANS
n_coffee = a_coffee // 15 #  g // *n_ stands for `number`

print("Write how many cups of coffee you will need:")
cups = int(input("> "))  # number of coffee cups the user wants to prepare

amounts = [n_water, n_milk, n_coffee]
# The smallest number of the list of ingredient is the limiter for the output
i_limiter = min(amounts)  # *i_ stands for `ingredient`

if i_limiter == cups:
    print(f"Yes, I can make that amount of coffee")
elif i_limiter > cups:
    print(f"Yes, I can make that amount of coffee (and even {i_limiter - cups} more than that)")
else:
    print(f"No, I can make only {i_limiter} cups of coffee")
'''


# -------------------- STAGE #4 & #5 & #6 --------------------------

class CoffeeMachine:
    # Machine information:
    def __init__(self):
        self.water = 400  # ml
        self.milk = 540  # ml
        self.coffee_beans = 120  # g
        self.cups = 9  # disposable cups
        self.money = 550  # US$
        self.action = None

    def main(self):
        while True:
            self.machine_options()
            if self.action == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                buy = input("> ")
                if buy == "1" and self.machine_check(buy):  # espresso
                    self.water -= 250  # ml
                    self.coffee_beans -= 16  # g
                    self.cups -= 1
                    self.money += 4
                elif buy == "2" and self.machine_check(buy):  # latte
                    self.water -= 350  # ml
                    self.milk -= 75  # ml
                    self.coffee_beans -= 20  # g
                    self.cups -= 1
                    self.money += 7
                elif buy == "3" and self.machine_check(buy):  # cappuccino
                    self.water -= 200  # ml
                    self.milk -= 100  # ml
                    self.coffee_beans -= 12  # g
                    self.cups -= 1
                    self.money += 6
                else:  # back to menu
                    continue
            elif self.action == "fill":
                print("Write how many ml of water do you want to add:")
                self.water += int(input("> "))
                print("Write how many ml of milk do you want to add:")
                self.milk += int(input("> "))
                print("Write how many grams of coffee beans do you want to add:")
                self.coffee_beans += int(input("> "))
                print("Write how many disposable cups of coffee do you want to add:")
                self.cups += int(input("> "))
                print()
            elif self.action == "take":
                print(f"I gave you ${self.money}")
                print()
                self.money = 0
            elif self.action == "remaining":
                self.machine_info()
                print()
            elif self.action == "exit":
                break
            else:
                continue

    def machine_info(self):
        print(f'''
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money'''
              )

    def machine_options(self):
        print("Write action (buy, fill, take, remaining, exit):")
        self.action = input("> ")
        return self.action

    def machine_check(self, buy):
        if buy == "1":  # espresso
            if self.water >= 250 and self.coffee_beans >= 16:
                print("I have enough resources, making you a coffee!\n")
                return True
            elif self.water < 250:
                print("Sorry, not enough water!\n")
                return False
            else:  # not enough coffee_beans
                print("Sorry, not enough coffee beans!\n")
                return False
        elif buy == "2":  # latte
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20:
                print("I have enough resources, making you a coffee!\n")
                return True
            elif self.water < 350:
                print("Sorry, not enough water!\n")
                return False
            elif self.milk < 75:
                print("Sorry, not enough milk!\n")
                return False
            else:  # not enough coffee beans
                print("Sorry, not enough coffee beans!\n")
                return False
        elif buy == "3":  # cappuccino
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12:
                print("I have enough resources, making you a coffee!\n")
                return True
            elif self.water < 200:
                print("Sorry, not enough water!\n")
                return False
            elif self.milk < 100:
                print("Sorry, not enough milk!\n")
                return False
            else:  # for coffee beans
                print("Sorry, not enough coffee beans!\n")
                return False


coffee_please = CoffeeMachine()
# Now coffee_please has a self.water; self.milk; self.coffee_beans; self.cups
# also self.money and self.action!
coffee_please.main()
