class Date:
    def __init__(self, day, date, month, year):
        self.day = day
        self.date = date
        self.month = month
        self.year = year

    def __str__(self):
        days = [0, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        months = [0, "January", "February", "March", "April", "May", "June", "July", "August", "September",
                  "October", "November", "December"]
        return days[self.day] + ' ' + str(self.date) + ', ' + months[self.month] + ' ' + str(self.year) + '.'
