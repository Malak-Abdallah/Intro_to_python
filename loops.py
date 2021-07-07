# The provided code stub reads and integer, , from STDIN. For all non-negative integers i< n , print square value of i
# 1 <= n <= 20
if __name__ == '__main__':
    n = int(input("Enter a positive value less than 20 \n"))
    for i in range(n):
        print(str(i ** 2))
