'''
from math import ceil, log


class LoanCalculator:
    def __init__(self):
        self.option = None
        self.questions = None
        self.loan_principal = None
        self.num_of_periods = None
        self.loan_interest = None
        self.monthly_payment = None
        self.annuity_payment = None

    def A(self):
        P, i, n = self.loan_principal, self.loan_interest, self.num_of_periods
        dividend = i * pow((1 + i), n)
        divisor = pow((1 + i), n) - 1
        return P * (dividend / divisor)

    def n(self):
        A, i, P = self.monthly_payment, self.loan_interest, self.loan_principal
        x = A / (A - i * P)
        return ceil(log(x, (1 + i)))

    def P(self):
        A, i, n = self.annuity_payment, self.loan_interest, self.num_of_periods
        dividend = i * pow((1 + i), n)
        divisor = pow((1 + i), n) - 1
        return A / (dividend/divisor)

    def calculator(self):
        self.option = input('What do you want to calculate?\n'
                            'type "n" for number of monthly payments,\n'
                            'type "a" for annuity monthly payment amount,\n'
                            'type "p" for loan principal:\n')
        if self.option == "n":
            self.loan_principal = float(input("Enter the loan principal:\n"))
            self.monthly_payment = float(input("Enter the monthly payment:\n"))
            self.loan_interest = float(input("Enter the loan interest:\n")) / (12 * 100)
            n = self.n()
            print(' '.join(f"It will take {n // 12 if n // 12 != 0 else ''} "
                           f"{'years' if n // 12 > 1 else ('' if n // 12 <= 0 else 'year')} "
                           f"{'and' if n // 12 > 0 and n % 12 > 0 else ''} {n % 12 if n % 12 != 0 else ''} "
                           f"{'months' if n % 12 > 1 else ('' if n % 12 <= 0 else 'month')} to repay this loan!".split()))
        elif self.option == "a":
            self.loan_principal = float(input("Enter the loan principal:\n"))
            self.num_of_periods = float(input("Enter the number of periods:\n"))
            self.loan_interest = float(input("Enter the loan interest:\n")) / (12 * 100)
            a = self.A()
            print(f"Your monthly payment = {ceil(a)}!")
        elif self.option == "p":
            self.annuity_payment = float(input("Enter the annuity payment:\n"))
            self.num_of_periods = float(input("Enter the number of periods:\n"))
            self.loan_interest = float(input("Enter the loan interest:\n")) / (12 * 100)
            p = self.P()
            print(f"Your loan principal = {p}!")


calc1 = LoanCalculator()
calc1.calculator()
'''
# ----------------------------------------- STAGE 4 ------------------------------------- #
import argparse
from math import ceil, log
from sys import argv, exit

# handling the CLI arguments!
parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()
parser.add_argument("--type")
parser.add_argument("--payment", type=float, default=0)
parser.add_argument("--principal", type=float, default=0)
parser.add_argument("--periods", type=int, default=0)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

# handling all exceptions and errors!
if not args.type or not args.interest or (args.type == "diff" and args.payment) \
        or len(argv) != 5 or args.payment < 0 or args.principal < 0 \
        or args.periods < 0 or args.interest < 0:
    print("Incorrect parameters")
    exit(1)


class LoanCalculator:
    def __init__(self):
        self.loan_principal = None
        self.num_of_periods = None
        self.loan_interest = None
        self.monthly_payment = None
        self.annuity_payment = None
        self.overpayment = 0

    def A(self):
        P, i, n = self.loan_principal, self.loan_interest, self.num_of_periods
        dividend = i * pow((1 + i), n)
        divisor = pow((1 + i), n) - 1
        return P * (dividend / divisor)

    def n(self):
        A, i, P = self.monthly_payment, self.loan_interest, self.loan_principal
        x = A / (A - i * P)
        return ceil(log(x, (1 + i)))

    def P(self):
        A, i, n = self.annuity_payment, self.loan_interest, self.num_of_periods
        dividend = i * pow((1 + i), n)
        divisor = pow((1 + i), n) - 1
        return A / (dividend/divisor)

    def Dm(self):
        P, i, n = self.loan_principal, self.loan_interest, self.num_of_periods
        for m in range(1, n + 1):
            diff = ceil(P / n + i * (P - ((P * (m - 1)) / n)))
            self.overpayment += diff
            print(f"Month {m}: payment is {diff}")

    def calculator(self):
        if args.type == "annuity":
            # to calc the months needed for payment completion
            if args.principal and args.payment and args.interest:
                self.loan_principal = args.principal
                self.monthly_payment = args.payment
                self.loan_interest = args.interest / (12 * 100)
                n = self.n()
                print(' '.join(f"It will take {n // 12 if n // 12 != 0 else ''} "
                       f"{'years' if n // 12 > 1 else ('' if n // 12 <= 0 else 'year')} "
                       f"{'and' if n // 12 > 0 and n % 12 > 0 else ''} {n % 12 if n % 12 != 0 else ''} "
                       f"{'months' if n % 12 > 1 else ('' if n % 12 <= 0 else 'month')} to repay this loan!".split()))
                print(f"Overpayment = {int(self.monthly_payment * n - self.loan_principal)}")
            elif args.principal and args.periods and args.interest:
                self.loan_principal = args.principal
                self.num_of_periods = args.periods
                self.loan_interest = args.interest / (12 * 100)
                a = self.A()
                print(f"Your annuity payment = {ceil(a)}!")
                print(f"Overpayment = {round(ceil(a) * self.num_of_periods - self.loan_principal)}")
            elif args.payment and args.periods and args.interest:
                self.annuity_payment = args.payment
                self.num_of_periods = args.periods
                self.loan_interest = args.interest / (12 * 100)
                p = int(self.P())
                print(f"Your loan principal = {p}!")
                print(f"Overpayment = {int(self.annuity_payment * self.num_of_periods - p)}")
        elif args.type == "diff":
            self.loan_principal = args.principal
            self.num_of_periods = args.periods
            self.loan_interest = args.interest / (12 * 100)
            self.Dm()
            print(f"\nOverpayment = {round(self.overpayment - self.loan_principal)}")


calc1 = LoanCalculator()
calc1.calculator()
