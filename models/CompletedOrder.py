import itertools


class CompletedOrder:
    newId = itertools.count()

    def __init__(self, title, time, price, staff, ):
        self.id = next(self.newId) + 1
        self.staff = staff
        self.price = price
        self.time = time
        self.title = title

    def __str__(self):
        return "Order: " + str(self.id) + "\nTitle: " + self.title + "\nTook: " + str(self.time) + " days"
