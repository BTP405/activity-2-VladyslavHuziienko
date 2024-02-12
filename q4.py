def decorator(func):
    """Printing numbers statistic"""
    def wrapper(line):
        data = func(line)
        print(f"Numbers: {data}")
        print(f"Numbers count: {len(data)}")
        print(f"Average of the numbers: {sum(data)/len(data)}")
        print(f"Maximum of the numbers: {max(data)}\n")
    return wrapper

@decorator
def print_line(line):
    """Printing a line"""
    nums = line.split(' ')
    nums = [int(x) for x in nums]
    return nums

def printStats(t):
    """Openning a file"""
    file = open(t)

    if file.closed == False:
        line = file.readline()

        """Reading line by line"""
        while len(line):
            print_line(line)
            
            line = file.readline()
    else:
        print("Error opening a file")


printStats('./q4_data.txt')