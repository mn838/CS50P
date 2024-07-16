from project import create_account, withdraw, deposit

def test_function_1():
    bank_list = create_account(100, "Checking", 1)
    assert bank_list[0].amount == 100
    assert bank_list[0].type_of_account == "Checking"
    assert bank_list[0].account_number == 1


def test_function_2():
    bank_list = create_account(100, "Checking", 2)
    deposit(50, 2)
    assert bank_list[1].amount == 150
    assert bank_list[1].type_of_account == "Checking"
    assert bank_list[1].account_number == 2


def test_function_n():
    bank_list = create_account(100, "Checking", 3)
    withdraw(50, 3)
    assert bank_list[2].amount == 50
    assert bank_list[2].type_of_account == "Checking"
    assert bank_list[2].account_number == 3
