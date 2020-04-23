class Order:
    # These are the attributes that each order must have to be initialised
    def __init__(self, title, time, assigned_to, priority):
        self.title = title
        self.time = time
        self.assigned_to = assigned_to
        self.priority = priority
