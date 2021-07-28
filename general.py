from itertools import permutations

if __name__ == '__main__':
    word=list(map(str,input().split(" ")))
    len = int(word[1])
    per=permutations(list(word[0]),len)
    arr=sorted(per)

    for x in arr:
        strr=x[0]+x[1]
        print(strr)




