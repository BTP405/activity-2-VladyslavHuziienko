import matplotlib.pyplot as plt

def getRange(n):
    """Returns range key based on number n"""
    if n >= 0 and n <= 10:
        return "0-10cms"
    if n >= 11 and n <= 20:
        return "11-20cms"
    if n >= 21 and n <= 30:
        return "21-30cms"
    if n >= 31 and n <= 40:
        return "31-40cms"
    if n >= 41 and n <= 50:
        return "41-50cms"

def graphSnowfall(t):
    """Read data from the file and display a plot with number of occurrences

        This function reads the file t, and writes amount of occurrences in to the dictionary, and plots that data.
        The generated plot is saved to snowfall_data.png file.
    """
    file = open(t)
    data = {"0-10cms": 0, "11-20cms": 0, "21-30cms": 0, "31-40cms": 0, "41-50cms": 0}
    if file.closed == False:
        line = file.readline()
        while len(line):
            num = int(line)

            num_range = getRange(num)

            data[num_range] += 1

            line = file.readline()

        plt.bar(data.keys(), data.values(), width = 0.5)
        plt.xlabel("Ranges")
        plt.ylabel("Occurrences")
        plt.title("Snowfall Data")
        plt.savefig('snowfall_data.png')

    else:
        print("Error opening a file")


graphSnowfall('./q2_data.txt')