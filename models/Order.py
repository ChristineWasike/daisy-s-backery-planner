class Order:

    # These are the attributes that each order must have to be initialised
    def __init__(self, title, time, assigned_to, priority_code, status):
        self.title = title
        self.time = time
        self.labour = assigned_to
        self.code = priority_code
        self.status = status
