import menu_functions
import sys
import os


def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix-based systems (Linux, macOS, etc.)
    else:
        _ = os.system('clear')

menu_choice = 0
while menu_choice != 6:
    print('##### Pharmacy Inventory System ####')
    print('-----------------------------')
    print("|Enter 1 for Pharmacy menu  |")
    print('----------------------------')
    print('|Enter 2 for Customer menu  |')
    print('----------------------------')
    print('|Enter 3 for Supplier menu  |')
    print('----------------------------') 
    print('|Enter 4 for Report menu    |')
    print('----------------------------')
    print('|Enter 5 for Invoicing      |')
    print('----------------------------')
    print('|Enter 6 to Exit program|')
    print('-----------------------------')
    menu_choice = int(input("Enter Your Choice\n"))
    if menu_choice == 1:
        clear_terminal()
        menu_functions.medicine_menu()
    elif menu_choice == 2:
        clear_terminal()
        menu_functions.customer_menu()
    elif menu_choice == 3:
        clear_terminal()
        menu_functions.supplier_menu()
    elif menu_choice == 4:
        clear_terminal()
        menu_functions.report_menu()
    elif menu_choice == 5:
        clear_terminal()
        menu_functions.invoicing_menu()
    elif menu_choice == 6:
        clear_terminal()
        break
    else:
        print("Invalid Input! Try Again! \n")    
sys.exit()
