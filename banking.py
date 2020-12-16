import random
import sys
import sqlite3

# Constants are made `str` for the ease of concatenating them
# also because strings are IMMUTABLE in Python
MII, INN, CHECKSUM = "4", "400000", "?"

# SQLite3 Data Base
accounts = sqlite3.connect("card.s3db")
sql = accounts.cursor()

sql.execute(""" CREATE TABLE IF NOT EXISTS card(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0);""")

accounts.commit()

# To keep track of sessions
is_logged = False
card_num = "?"
card_pin = "?"


def luhn_checksum(card):
    """" Generates the CHECKSUM to validate a card number"""

    # to be able to change the value internally
    global CHECKSUM
    sum_ = 0

    for index, num in enumerate(card):
        num = int(num)
        # The algorithm takes even indices because indices start at `0`
        if index % 2 == 0:
            num *= 2
        if num > 9:
            num -= 9
        sum_ += num

    # If the 15-digits already sum to a number divisible by 10,
    # then `CHECKSUM` don't need to do anything! just be ZERO!
    CHECKSUM = str(10 - (sum_ % 10)) if (sum_ % 10) != 0 else str(0)


def create_account():
    """ Creates unique account number and pin """
    while True:
        # Changes seed according to the current system time at every loop
        # For a less pseudo-random result!
        random.seed()
        # `account_number` is converted to `str` for the ease of
        # later concatenating all numbers to generate the card sequence
        # also because strings are IMMUTABLE in Python
        account_number = str(random.randrange(000000000, 999999999))
        # if first numbers are `zeros` 0, then they get filled into a `str`
        if len(account_number) < 9:
            account_number = account_number.zfill(9)
        # generating CHECKSUM
        luhn_checksum(INN + account_number)
        unique_card_num = INN + account_number + CHECKSUM
        # checks if card number is already taken, 
        # if it is, than tries another random sequence
        sql.execute(f"SELECT * FROM card WHERE number={unique_card_num};")
        if bool(sql.fetchone()):
            continue
        # generating random 4 digit `str` PIN    
        pin = str(random.randrange(0000, 9999))
        # if length of pin is not 4, because of zeros in front
        # then we fill with zeros!
        if len(pin) < 4:
            pin = pin.zfill(4)
        # adding account to card table
        sql.execute(f"INSERT INTO card (number, pin) VALUES ({unique_card_num}, {pin});")
        accounts.commit()
        break

    # print profile
    print("\nYour card has been created\nYour card number:")
    print(f"{unique_card_num}\nYour card PIN:\n{pin}\n")


def login():
    """changes `is_logged` to True if login is successful"""

    # to be able to change the value internally
    global is_logged
    global card_num
    global card_pin

    card_num = input("\nEnter your card number:\n")
    card_pin = input("Enter your PIN:\n")

    # checks for account and pin in card table
    sql.execute(f"SELECT * FROM card WHERE number={card_num} AND pin={card_pin};")
    if bool(sql.fetchone()):
        print("\nYou have successfully logged in!\n")
        accounts.commit()
        is_logged = True
    else:
        print("\nWrong card number or PIN!\n")


def balance():

    sql.execute(f"SELECT balance FROM card WHERE number={card_num} AND pin={card_pin};")

    return sql.fetchone()[0]


def add_income():

    current_income = balance()
    new_income = int(input("\nEnter income:\n"))

    sql.execute(f"UPDATE card SET balance = {current_income + new_income}"
                f" WHERE number={card_num} AND pin={card_pin};")
    accounts.commit()

    print("Income was added!\n")


def do_transfer():

    card_trans = input("\nTransfer\nEnter card number:\n")

    # handling ERROR 1
    if card_trans == card_num:
        print("You can't transfer money to the same account!\n")
        return

    # Luhn's_algo to handle ERROR 2
    sum_ = 0
    for index, num in enumerate(card_trans):
        num = int(num)
        # The algorithm takes even indices because indices start at `0`
        if index % 2 == 0:
            num *= 2
        if num > 9:
            num -= 9
        sum_ += num

    if sum_ % 10 != 0:
        print("Probably you made a mistake in the card number. Please try again!\n")
        return

    sql.execute(f"SELECT balance FROM card WHERE number={card_trans};")

    other_balance = sql.fetchone()

    if other_balance:
        current_income = balance()
        transfer = int(input("Enter how much money you want to transfer:\n"))

        if transfer < current_income:
            sql.execute(f"UPDATE card SET balance = {other_balance[0] + transfer}"
                        f" WHERE number={card_trans};")
            sql.execute(f"UPDATE card SET balance = {current_income - transfer}"
                        f" WHERE number={card_num};")
            accounts.commit()
            print("Success!\n")
        else:
            # handling ERROR 4!
            print("Not enough money!\n")
    else:
        # handling ERROR 3!
        print("Such a card does not exist.\n")
        return


def close_account():

    global card_num
    global card_pin
    global is_logged

    sql.execute(f"DELETE FROM card WHERE number={card_num} AND pin={card_pin};")
    accounts.commit()
    card_num, card_pin = "?", "?"

    print("\nThe account has been closed!\n")

    is_logged = False


def logout():
    """ Resets `is_logged` to False """

    # to be able to change the value internally
    global is_logged

    print("\nYou have successfully logged out!\n")
    is_logged = False


while True:

    option_1 = "1. Create an account"
    option_2 = "2. Log into account"
    option_3 = "0. Exit"

    # First checks if user is already logged in
    # The menu changes depending on `is_logged` value
    if is_logged:
        option_1 = "1. Balance\n2. Add income\n3. Do transfer"
        option_2 = "4. Close account\n5. Log out"

    print(option_1 + "\n" + option_2 + "\n" + option_3)

    choice = input()

    if choice == "1":
        print(f"\nBalance: {balance()}\n") if is_logged else create_account()
    elif choice == "2":
        add_income() if is_logged else login()
    elif choice == "3" and is_logged:
        do_transfer()
    elif choice == "4" and is_logged:
        close_account()
    elif choice == "5":
        logout()
    elif choice == "0":
        print("\nBye!")
        sys.exit(0)
