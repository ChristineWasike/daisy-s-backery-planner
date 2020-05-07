import calendar as calendar
import time as time

from models.Stack import *
from util.DummyData import *
from models.BinarySearch import *
from models.CompletedOrder import *


# Handle Type Error Integer from User Input
def value_error_handler_integer(user_input):
    try:
        user_input_int = int(user_input)
        return user_input_int
    except ValueError:
        print("\nPlease enter integers only!!\n")
        return False


# General Program Function
# Function that keeps the program running depending on the users choice
def user_status_type():
    user_status = input("Do you want to continue? Y/N\n")
    if user_status == 'n' or user_status == 'no':
        exit()
    else:
        user_main_menu()
    return user_status


# Function that presents menu and deals with menu option
def user_main_menu():
    print("=====Welcome to Daisy's Planner=====")
    print("========= Menu Options =============")
    print("1. Enter Order\n"
          "2. View Orders\n"
          "3. Delete Orders\n"
          "4. Update Orders\n"
          "5. Clear Orders\n")
    userOption = input("Enter a number corresponding to the option you want:")
    user_option_int = value_error_handler_integer(userOption)
    if not user_option_int:
        pass
    else:
        if user_option_int == 1:
            enter_order()
            user_status_type()
        elif user_option_int == 2:
            view_orders()
            user_status_type()
        elif user_option_int == 3:
            delete_order()
            user_status_type()
        elif user_option_int == 4:
            update_order()
            user_status_type()
        elif user_option_int == 5:
            clear_order()
            user_status_type()
        else:
            print("The option you chose is invalid.")
            user_status_type()


# Function to collect instant variables and creates order instance
def enter_order():
    result = time.localtime()
    order_title = input("Enter the title: \n")
    order_due_date = pick_date()
    order_time_stamp = (result.tm_mday, result.tm_mon, result.tm_year)
    order_staff = input("How many people are assigned to this task?(enter a number) \n")
    order_staff_int = value_error_handler_integer(order_staff)
    order_code = set_enum_order("code")
    order_status = set_enum_order("status")
    order_price = input("Enter the price of this order:\n")
    order_price_int = value_error_handler_integer(order_price)
    new_order = Order(order_title, order_due_date, order_time_stamp, order_staff_int, order_code, order_status,
                      order_price_int)
    daisy_orders[new_order.id] = new_order
    date_collection[new_order.id] = new_order.due_date


# Function that displays the orders
def view_orders():
    view_by_str = input("View orders by:\n"
                        "1. Id\n"
                        "2. Title\n")

    view_by = value_error_handler_integer(view_by_str)
    if not view_by:
        pass
    if view_by == 1:
        for order in daisy_orders:
            print(str(order) + ". " + daisy_orders[order].title)
            view_order_details()
    elif view_by == 2:
        sort_orders_by_title()
        view_order_details()
    else:
        print("Invalid choice entered.")


# delete function that deletes orders from Daisy's scheduler in case a customer
def delete_order():
    view_orders()
    delete_str = input("Enter the corresponding number to delete an order?\n")
    delete = value_error_handler_integer(delete_str)
    for order in daisy_orders:
        if delete == daisy_orders[order].id:
            print(daisy_orders[order].title + " has been removed.")
            daisy_orders.pop(order)
            break


# update function that enables Daisy to make edits to the details of the order
def update_order():
    # Change attr order, Mini menu, view or search(linear)
    # Within the order they can edit the priority_code, status, assigned_to, due_date
    update_choice_str = input("Would you like to \n"
                              "1. View the orders \n"
                              "2. Search for the order by id\n"
                              "3. Search for the order by title\n")

    update_choice = value_error_handler_integer(update_choice_str)
    if not update_choice:
        pass
    if update_choice == 1:
        view_orders()
        user_order_choice_str = int(input("Enter the index of the order you would like to update:\n"))
        user_order_choice = value_error_handler_integer(user_order_choice_str)
        update_menu(user_order_choice)

    elif update_choice is 2:
        return search_by_order_id()

    elif update_choice is 3:
        return search_order_by_title()

    else:
        return "The option you entered is invalid"


# Searching orders by id
def search_by_order_id():
    user_order_choice_str = input("Enter the index of the order you would like to search for:\n")
    user_order_choice = value_error_handler_integer(user_order_choice_str)
    if binarySearch(list(daisy_orders.keys()), user_order_choice):
        update_menu(user_order_choice)
    else:
        print("Unable to find the order you're looking for.")


# Searching orders by title
def search_order_by_title():
    user_order_choice = input("Enter the title of the order you would like to search for:\n")
    list_of_titles_ids = []
    list_of_titles = []
    for order in daisy_orders:
        list_of_titles_ids.append([daisy_orders[order].title, order])
    sorted_list_of_titles_ids = sorted(list_of_titles_ids)
    order_id = [key for (value, key) in sorted_list_of_titles_ids if value == user_order_choice]

    for order in daisy_orders:
        list_of_titles.append(daisy_orders[order].title)
    sorted_list_of_titles = sorted(list_of_titles)

    if binarySearch(sorted_list_of_titles, user_order_choice):
        # TODO Might be temporary
        print("Item found.")
        update_menu(order_id[0])
    else:
        print("Unable to find the order you're looking for.")


# Function for the second menu
def update_menu(order_id):
    user_update_menu_choice_str = input("Here is what you can update:\n"
                                        "1. Priority Code\n"
                                        "2. Status\n"
                                        "3. Number of staff assigned to the order\n"
                                        "4. The order's due date\n")
    user_update_menu_choice = value_error_handler_integer(user_update_menu_choice_str)

    if not user_update_menu_choice:
        pass
    # Option that will update the priority code
    if user_update_menu_choice == 1:
        print("The current priority code is: " + daisy_orders[order_id].code)
        priority_code_update = input("Enter new code(Red, Yellow, Green): ")
        daisy_orders[order_id].code = priority_code_update
        print("Now " + daisy_orders[order_id].title + " has the code " + daisy_orders[order_id].code)

    # Option that will update an order's status
    elif user_update_menu_choice == 2:
        print("The current status is: " + daisy_orders[order_id].status)
        status_update = input("Enter new status(Pending, Ongoing, Complete): ")
        daisy_orders[order_id].status = status_update
        print("Now " + daisy_orders[order_id].title + " has the status " + daisy_orders[order_id].status)

    # Option that will update the number of people assigned to one order
    elif user_update_menu_choice == 3:
        print("The current status is: " + str(daisy_orders[order_id].staff))
        staff_update = input("Enter new number of staff assigned to the order: ")
        daisy_orders[order_id].staff = staff_update
        print("Now " + daisy_orders[order_id].title + " has " + str(daisy_orders[order_id].staff)
              + " staff members assigned to it")

    # Option that will change due date of an order
    elif user_update_menu_choice == 4:
        print("The current due date is: " + display_order_date(daisy_orders[order_id].due_date))
        print("Enter new date below:\n")
        updated_date = pick_date()
        daisy_orders[order_id].due_date = updated_date
        print("Now " + daisy_orders[order_id].title + " is due on "
              + display_order_date(daisy_orders[order_id].due_date))
    else:
        return "The option you entered is invalid"


# mark_as_done function that moves all completed orders to the paid list
def clear_order():
    order_status_list = [Status(1), Status(2), Status(3)]
    view_orders()
    user_input = int(input("Enter the number corresponding to the order: "))
    order_id_list = list(daisy_orders.keys())
    if binarySearch(order_id_list, user_input):
        print("The order " + daisy_orders[user_input].title + " is going to be cleared.")
        daisy_orders[user_input].status = order_status_list[2]
        order_title = daisy_orders[user_input].title
        order_price = daisy_orders[user_input].price
        new_status = daisy_orders[user_input].status
        order_staff = daisy_orders[user_input].staff
        d0 = daisy_orders[user_input].time_stamp.day
        d1 = daisy_orders[user_input].due_date.day
        order_time = d0 - d1
        cleared_order = CompletedOrder(order_title, order_time, order_price, order_staff)
        print(cleared_order)


# This function was added get the date input from the user
def date_day(month, year):
    day_str = input("Enter the order's due day(1-7): ")
    day = value_error_handler_integer(day_str)
    date_str = input("Enter the order's due date(1-31): ")
    date = value_error_handler_integer(date_str)
    if 1 <= day <= 7 and 1 <= date <= 31:
        order_full_date = Date(day, date, month, year)
        return order_full_date
    else:
        print("Sorry, invalid date or day. Please try again.")
        return date_day(month, year)


# Function that gets the date from the user
def pick_date():
    result = time.localtime()

    # Give the user the option if it is towards the end of the month to place to order to the following month

    if 25 < result.tm_mday < 31:
        user_input = input("Is the order due next month?(Yes/No)")
        # Display next month and get user input
        if user_input == "yes" or user_input == "Yes":
            print(calendar.month(result.tm_year, result.tm_mon + 1))
            return date_day(result.tm_mon, result.tm_year)
        # Display current month and get user input
        elif user_input == "no" or user_input == "No":
            print(calendar.month(result.tm_year, result.tm_mon))
            return date_day(result.tm_mon, result.tm_year)
        else:
            return "The option you entered is invalid"

    else:
        print(calendar.month(result.tm_year, result.tm_mon))
        return date_day(result.tm_mon, result.tm_year)


# Function to print the date in a user friendly way
def display_order_date(date_array):
    week_day = ""
    day = date_array[0]
    if day == 1:
        week_day = "Monday"
    elif day == 2:
        week_day = "Tuesday"
    elif day == 3:
        week_day = "Wednesday"
    elif day == 4:
        week_day = "Thursday"
    elif day == 5:
        week_day = "Friday"
    elif day == 6:
        week_day = "Saturday"
    elif day == 7:
        week_day = "Sunday"
    else:
        return None
    return week_day + " " + str(date_array[1]) + "-" + str(date_array[2]) + "-" + str(date_array[3])


# Function sort by that will sort orders according to the priority code or date
# TODO sort by priority code or date using switch
# TODO sort functions (by code and due_date)
def sort_orders():
    pass


def sort_orders_by_title():
    list_of_titles_ids = []
    for order in daisy_orders:
        list_of_titles_ids.append([daisy_orders[order].title, order])
    sorted_list_of_titles_ids = sorted(list_of_titles_ids)

    for order in sorted_list_of_titles_ids:
        print(str(order[1]) + ". " + order[0] + ".")


def sort_orders_by_priority_code():
    list_by_priority = []
    for order in daisy_orders:
        list_by_priority.append(
            [daisy_orders[order].code.value, daisy_orders[order].code.name, daisy_orders[order].title, order])
    sorted_list_by_priority = sorted(list_by_priority)

    for order in sorted_list_by_priority:
        print(str(order[3]) + ". " + order[2] + "(" + order[1] + ").")


def sort_orders_by_status():
    pass


def view_order_details():
    order_details_choice = input("\nWould you like to view details of a specific order? Y/N\n").lower()

    if order_details_choice == "y" or order_details_choice == order_details_choice == "yes" or order_details_choice == \
            "yeah" or order_details_choice == "yah":
        order_id_str = input("Kindly type in the order id(integer) of the order here:\n")
        order_id = value_error_handler_integer(order_id_str)
        # TODO I have repeated code from line 139
        if binarySearch(list(daisy_orders.keys()), order_id):
            return daisy_orders.get(order_id).display_order()
    elif order_details_choice == "n" or order_details_choice == order_details_choice == "no" or order_details_choice == \
            "nope" or order_details_choice == "nah":
        pass
    else:
        pass


# Function that returns enum values for each order's priority code and status
def set_enum_order(instance_var):
    priority_code_list = [PriorityCode(1), PriorityCode(2), PriorityCode(3)]
    order_status_list = [Status(1), Status(2), Status(3)]
    if instance_var == "code":
        user_input = input("Enter order code(Red, Yellow, Green):\n").capitalize()
        if user_input == priority_code_list[0].name:
            return priority_code_list[0].name
        elif user_input == priority_code_list[1].name:
            return priority_code_list[1].name
        elif user_input == priority_code_list[2].name:
            return priority_code_list[2].name
        else:
            return "The code you entered is invalid"
    elif instance_var == "status":
        user_input = input("Enter order status(Pending, Ongoing, Completed): \n")
        if user_input == order_status_list[0].name:
            return order_status_list[0].name
        elif user_input == order_status_list[1].name:
            return order_status_list[1].name
        elif user_input == order_status_list[2].name:
            return order_status_list[2].name
        else:
            return "The code you entered is invalid"
