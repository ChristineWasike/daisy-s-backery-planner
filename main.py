"""
Here, we need to run the entire scheduler from when Daisy inputs her orders,
when she views the orders she has for the week, updates the order based on
what she's been able to work on to clearing orders upon successful delivery and payment.
"""

# TODO run the entire program from here

from util.functions import *

# user_main_menu()
# enter_order()

my_order = Order("Coffee Muffin", "12-05-2020", "Daisy", "High Priority", "Pending")
print(my_order.title, my_order.status)
my_order.status = "Ongoing"
print(my_order.title, my_order.status)

i = input("Please enter name[Jack]:")
