import calendar
import time
import array as arr
from models.Order import *

# Some Dummy orders to test some of the functions
# TODO add the months here Rachel
order1 = Order("Birthday1", (3, 21, 5, 2020), (7, 20, 7, 2020), 2, "red", "started", 1000)
order2 = Order("Birthday2", (1, 11, 5, 2020), (7, 20, 7, 2020), 1, "yellow", "started", 1000)
order3 = Order("Birthday3", (7, 30, 5, 2020), (7, 20, 7, 2020), 2, "red", "started", 20000)
order4 = Order("party1", (2, 1, 5, 2020), (7, 20, 7, 2020), 2, "red", "started", 32000)
order5 = Order("Wedding1", (5, 12, 5, 2020), (7, 20, 7, 2020), 1, "green", "started", 25000)
order6 = Order("Wedding2", (6, 17, 5, 2020), (7, 20, 7, 2020), 1, "yellow", "started", 15000)

daisy_orders = {order1.id: order1, order2.id: order2, order3.id: order3,
                order4.id: order4, order5.id: order5, order6.id: order6}

date_collection = {order1.id: order1.due_date}


# General Program Function
# Function that keeps the program running depending on the users choice
def user_status_type():
    user_status = input("Do you want to continue? Y/N\n").lower()
    if user_status == 'n' or user_status == 'no':
        exit()
    return user_status


# Function that presents menu and deals with menu option
def user_main_menu():
    print("=====Welcome to Daisy's Planner=====")
    print("========= Menu Options =============")
    print("1. Enter Order\n" +
          "2. View Orders\n" +
          "3. Delete Orders\n" +
          "4. Update Orders\n"
          "5. Clear Orders\n")
    userOption = int(input("Enter a number corresponding to the option you want:"))
    if userOption == 1:
        enter_order()
        user_status_type()
    elif userOption == 2:
        view_orders()
        user_status_type()
    elif userOption == 3:
        delete_order()
        user_status_type()
    elif userOption == 4:
        update_order()
        user_status_type()
    elif userOption == 2:
        clear_order()
        user_status_type()
    else:
        print("The option you chose is invalid.")


# Function to collect instant variables and creates order instance
def enter_order():
    result = time.localtime()
    order_title = input("Enter the title: \n")
    order_due_date = pick_date()
    order_time_stamp = (result.tm_mday, result.tm_mon, result.tm_year)
    order_labour = int(input("How many people are assigned to this task?(enter a number) \n"))
    order_code = input("Enter order code(Red, Yellow, Green):\n")
    order_status = input("Enter order status: \n")
    # TODO 3 options for the status
    order_price = int(input("Enter the price of this order:\n"))
    new_order = Order(order_title, order_due_date, order_time_stamp, order_labour, order_code, order_status,
                      order_price)
    daisy_orders[new_order.id] = new_order


# Function that displays the orders
# TODO sort the ids and display in ascending order
def view_orders():
    for order in daisy_orders:
        print(str(order) + ". " + daisy_orders[order].title)


# delete function that deletes orders from Daisy's scheduler in case a customer
def delete_order():
    view_orders()
    delete = input("Which order do you want to delete?\n")
    for order in daisy_orders:
        if delete == order:
            print(daisy_orders[order].title + " has been removed.")
            daisy_orders.pop(order)
            break


# update function that enables Daisy to make edits to the details of the order
def update_order():
    # Change attr order, Mini menu, view or search(linear)
    # Within the order they can edit the priority_code, status, assigned_to, due_date
    update_choice = int(input("Would you like to \n"
                              "1. View the orders \n"
                              "2. Search for the order by id\n"))
    if update_choice == 1:
        view_orders()
        user_order_choice = int(input("Enter the index of the order you would like to update:\n"))
        update_menu(user_order_choice)

    elif update_choice is 2:
        pass
    else:
        return "The option you entered is invalid"


# Function for the second menu
def update_menu(order_id):
    user_update_menu_choice = int(input("Here is what you can update:\n"
                                        "1. Priority Code\n"
                                        "2. Status\n"
                                        "3. Number of staff assigned to the order\n"
                                        "4. The order's due date\n"))
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
        print("The current status is: " + str(daisy_orders[order_id].labour))
        labour_update = input("Enter new number of staff assigned to the order: ")
        daisy_orders[order_id].labour = labour_update
        print("Now " + daisy_orders[order_id].title + " has " + str(daisy_orders[order_id].labour)
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
    pass


# Comment
# TODO I need help figuring out how to store the dates in a dictionary. Key? value?
def date_day(month, year):
    day = int(input("Enter the order's due day(1-7): "))
    date = int(input("Enter the order's due date(1-31): "))
    if 1 <= day <= 7 and 1 <= date <= 31:
        order_full_date = arr.array('i', [day, date, month, year])
        print(order_full_date)
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


# Function sort by that will sort orders according to the priority code or date
# TODO sort by priority code or date using switch


# Function to print the date
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


