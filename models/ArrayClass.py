class ArrayClass:
    def __init__(self, my_array):
        self.my_array = my_array

    # method that will count the items in a array and return the length
    def my_array_length(self):
        counter = 0
        # iterate through array counting elements
        for x in self.my_array:
            counter = counter + 1
        return counter

    # method to retrieve a particular element
    def my_array_get(self, index):
        if index > self.my_array_length():
            return "The index you enter is out of bonds"
        else:
            return self.my_array[index]

    # method that replace a value with another at a particular index
    def my_array_replace(self, index, value):
        # pop the value at the chosen index
        self.my_array.pop(index)
        # insert user value in space that was freed
        self.my_array.insert(index, value)
        return self.my_array