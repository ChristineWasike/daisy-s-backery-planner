import enum
import itertools
from util.functions import *


class Order:
    newId = itertools.count()

    # These are the attributes that each order must have to be initialised
    def __init__(self, title, due_date, time_stamp, assigned_to, priority_code, status, price):
        self.id = next(self.newId) + 1
        self.title = title
        self.due_date = due_date
        self.time_stamp = time_stamp
        self.staff = assigned_to
        self.code = priority_code
        self.status = status
        self.price = price

    def display_order(self):
        print("========Order Details========")
        print("Title: " + self.title)
        print("Due date: " + display_order_date(self.due_date))
        print("Order was made on: " + display_order_date(self.time_stamp))
        print("Priority code: " + self.code)
        print("Status: " + self.status)
        print("Assigned to: " + str(self.staff))
        print("Price(Rwf): " + str(self.price))


class PriorityCode(enum.Enum):
    Red = 1
    Yellow = 2
    Green = 3


class Status(enum.Enum):
    Pending = 1
    Ongoing = 2
    Complete = 3


