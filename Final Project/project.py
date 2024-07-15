
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
        if self.amount > amount:
            return ValueError("Amount Invalid")
        self.amount -= amount


def main() -> None:
    user_choice = 0
    bank_list = []
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
            try:
                user_input = input().split(" ")
                if int(user_input[0]) < 0:
                    print("Invalid Amount")
                    continue
                if user_input[1] != 'Checking' and user_input[1] != 'Savings':
                    print("Invalid Account Type")
                    continue
                bank_list.append(Bank(int(user_input[0]), user_input[1], account_number))
                print(bank_list)
                account_number += 1
            except:
                print("Account not made")
                continue

        if (user_choice == 2):
            try:
                amount = int(input("Enter withdrawal Amount (cannot be less than zero): "))
                if amount < 0:
                    print("Invalid amount")
                    continue
                account = bank_list[int(input("Enter account number: ")) - 1]
                account.withdraw(amount)
            except:
                print("account does not exist")
                continue

        if (user_choice == 3):
            try:
                amount = int(input("Enter deposit Amount (cannot be less than zero): "))
                if amount < 0:
                    print("Invalid amount")
                    continue
                account = bank_list[int(input()) - 1]
                account.deposit(amount)
            except:
                print("account does not exist")
                continue


        if (user_choice == 4):
            account = bank_list[int(input()) - 1]
            print(account)

        if (user_choice == 5):
            break

if __name__ == "__main__":
    main()
