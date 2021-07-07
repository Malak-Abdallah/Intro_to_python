# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input("Enter the first integer value "))
    b = int(input("Enter the second integer value "))

    print("The sum of the two values is : ", a + b)
    print("The difference between the two values is : ", a - b)
    print("The product of the two values is : ", a * b)

    # TASK 2:
    # Add logic to print two lines. The first line should contain the result of integer division, a // b.
    # The second line should contain the result of float division, a / b.
    # No rounding or formatting is necessary.
    print("the integer result of the division: ", int(a / b))
    print("the float result of the division: ", a / b)

    # we can add also different types of numbers like complex numbers
    img = 4j
    complexNum = 2+ 5j
    print("The new complex number is ", img+complexNum)
