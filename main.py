"""
Here, we need to run the entire scheduler from when Daisy inputs her orders,
when she views the orders she has for the week, updates the order based on
what she's been able to work on to clearing orders upon successful delivery and payment.
"""

# TODO run the entire program from here
from util.functions import *


# user_status = 'yes'
# while user_status == 'yes':
#     user_main_menu()

# display_order_details(1)
# a_list = [1, 2, 3, 4]
# print(a_list[0])
print(update_order())
# my_code = [PriorityCode(1), PriorityCode(2), PriorityCode(3)]
# count = 0
# for x in my_code:
#     print(my_code[count].name)
#     count += 1
list_of_keys = [key for (key, value) in daisy_orders.items() if value == title]
print(daisy_orders.items())