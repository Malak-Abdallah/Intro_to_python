# comments are written in this way!
# codes written here are solutions for solving problems from Hacker Rank.
# -------------------------------------------
# Jenan Queen 
if __name__ == '__main__':
    print("Hello there!! \nThis code to practise some basics in python. \n ")
    str = "Hello world"
    print(str[2:])
    # TASK 1:
    # If n is odd, print Weird
    # If n is even and in the inclusive range of 2 to 5, print Not Weird
    # If n is even and in the inclusive range of 6 to 20, print Weird
    # If n is even and greater than 20, print Not Weird
    # 1<= n <= 100
    print("Enter an integer greater then zero and less or equal 100 ")
    n = int(input().strip())
    if (n % 2) != 0:
        print("Weird")
    elif n % 2 == 0:
        if n in range(2, 6) or n > 20:
            print("Not Weird")
        else:
            print("Weird")
            
