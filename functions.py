# TASK 1:
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True,
# otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
# It is only necessary to complete the is_leap function.

# TASK 2:
# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following: 123...n

def is_leap(year):
    leap = False  # initialized a boolean variable
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap


def task2(n):
    for i in range(1, n + 1):
        print(i, end="")


if __name__ == '__main__':
    year = int(input("Enter a year\n"))
    n = int(input("Enter a positive integer for the second task\n"))
    print(is_leap(year))
    task2(n)
