import calendar
import time
from models.Order import *


# General Program Function


def user_main_menu():
    print("=====Welcome to Daisy's Planner=====")
    print("========= Menu Options =============")
    print("1. Enter Order\n" +
          "2. View Orders\n")
    userOption = int(input("Enter a number corresponding to the option you want:"))
    if userOption == 1:
        enter_order()
    elif userOption == 2:
        view_orders()
    else:
        print("The option you chose is invalid.")


def enter_order():
    order_title = input("Enter the title: \n")
    #     TODO Figure out how to store the day and date. Tuple? list?
    order_date = pick_date()
    order_labour = int(input("How many people are assigned to this task?(enter a number) \n"))
    #     TODO I need help with enum
    order_code = input("Enter order code(Red, Yellow, Green): \n")
    order_status = input("Enter order status: \n")
    new_order = Order(order_title, order_date, order_labour, order_code, order_status)


def view_orders():
    pass


# Function that gets the date from the user
def pick_date():
    result = time.localtime()
    # Give the user the option if it is towards the end of the month to place to order to the next month
    if 25 < result.tm_mday < 31:
        user_input = input("Is the order due next month?(Yes/No)")
        # Display next month and get user input
        if user_input == "yes" or user_input == "Yes":
            print(calendar.month(result.tm_year, result.tm_mon + 1))
            day = int(input("Enter the order's due day(1-7): "))
            date = int(input("Enter the order's due date(1-31): "))
            return day, date
        # Display current month and get user input
        elif user_input == "no" or user_input == "No":
            print(calendar.month(result.tm_year, result.tm_mon))
            day = int(input("Enter the order's due day(1-7): "))
            date = int(input("Enter the order's due date(1-31): "))
            return day, date
        else:
            return "The option you entered is invalid"
