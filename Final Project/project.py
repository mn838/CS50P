bank_list = []

class Bank:
    def __init__(self, amount = 0, type_of_account = "Checking", account_number = 0):
        self.amount = amount
        self.type_of_account = type_of_account
        self.account_number = account_number

    def get_amount(self):
        return self.amount

    def get_type(self):
        return self.type_of_account

    def __str__(self):
        return f'{self.type_of_account} account {self.account_number} has ${self.amount}'

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if self.amount < amount:
            return ValueError("Amount Invalid")
        self.amount -= amount


def create_account(initial_deposit: int, type_of_account: str, account_number: int):
    try:
        if initial_deposit < 0:
            print("Invalid Amount")
            return
        if type_of_account != 'Checking' and type_of_account != 'Savings':
            print("Invalid Account Type")
            return
        bank_list.append(Bank(initial_deposit, type_of_account, account_number))
    except:
        print("Account not made")
        return
    return bank_list


def withdraw(amount: int, account_number: int):
    try:
        if amount < 0:
            print("Invalid amount")
            return
        account = bank_list[account_number - 1]
        if amount > account.amount:
            print("Not enough funds")
            return
        account.withdraw(amount)
    except:
        print("account does not exist")
        return


def deposit(amount: int, account_number: int):
    try:
        if amount < 0:
            print("Invalid amount")
            return
        account = bank_list[account_number - 1]
        account.deposit(amount)
    except:
        print("account does not exist")
        return

def main() -> None:
    user_choice = 0
    account_number = 1

    while(True):
        print("[1] to create an account")
        print("[2] to withdraw")
        print("[3] to deposit")
        print("[4] to print account")
        print("[5] to quit program")
        user_choice = int(input())

        if (user_choice == 1):
            print("please input deposit amount and type of account (Checking, Savings)")
            user_input = input().split(" ")
            try:
                initial_amount = int(user_input[0])
            except:
                print("Invalid initial deposit")
                continue

            try:
                type_of_account = user_input[1]
            except:
                print("Incorrect arguments")
                continue

            create_account(initial_amount, type_of_account, account_number)
            if len(bank_list) == account_number:
                account_number += 1

        if (user_choice == 2):
            try:
                amount = int(input("Enter amount to withdraw: "))
                account = int(input("Enter your account number: "))
            except:
                print("Invalid datatypes")
                continue
            withdraw(amount, account)

        if (user_choice == 3):
            try:
                amount = int(input("Enter amount to withdraw: "))
                account = int(input("Enter your account number: "))
            except:
                print("Invalid datatypes")
                continue
            deposit(amount, account)


        if (user_choice == 4):
            account = bank_list[int(input("Enter account_number: ")) - 1]
            print(account)

        if (user_choice == 5):
            break

if __name__ == "__main__":
    main()
