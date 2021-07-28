# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
def check(numb):
    rev=numb[::-1]
    if rev[0]=="0":
        rev=rev.removeprefix("0")
    if rev[-1]=="-":
        print("-"+rev.replace("-",""))
    else:
        print(rev)



if __name__ == '__main__':
    inp = input("enter any signed number")
    check(inp)
