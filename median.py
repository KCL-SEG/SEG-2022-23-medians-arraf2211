"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def sort(number):
        sortedlist = sorted(number)
            x = len(sortedlist)
                if (len(sortedlist)%2):
                    median = sortedlist[int((x - 1) / 2)]
                    print(median)
                else:
                    index = (x / 2)
                    median = (sortedlist[int(index)-1] + sortedlist[int(index)]) /2
                    print(median)


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
sort(numbers)

