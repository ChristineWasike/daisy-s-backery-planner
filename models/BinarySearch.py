# Binary search function that takes in a sorted array and a value
def binarySearch(array, val):
    if len(array) > 0:
        # start and ending position in our array
        start = 0
        end = len(array) - 1

        # Loop through the array and find the midpoint
        while start <= end:
            midpoint = start + (end - start) // 2
            midValue = array[midpoint]
            # Case: the midpoint is the same as the value
            if midValue == val:
                return True
            # Case: the value is less than the midpoint then change the ending position
            elif val < midValue:
                end = midpoint - 1
            # Case: the value is less than the midpoint then change the starting position
            else:
                start = midpoint + 1

        return True
    else:
        return False
