# Number Analyzer Program
# This program performs basic operations on a list of numbers

def analyze_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


def main():
    numbers = []

    print("Enter 5 numbers:")

    for i in range(5):
        num = int(input(f"Number {i+1}: "))
        numbers.append(num)

    total, average, maximum, minimum = analyze_numbers(numbers)

    print("\nResults:")
    print("Total:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)


main()
