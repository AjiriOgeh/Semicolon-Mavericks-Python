from account import Account
from bank import Bank


def display_menu():
    main_menu = """Bank Menu
1.Register account
2.Deposit  
3.Withdraw
4.Transfer
5.Check balance
6.Close Account  
7.Exit"""
    return main_menu

def bank_app():
    print(display_menu())
    option = input("Select an option: ")
    print()
    match option:
        case "1":
