if __name__ == '__main__':
    x=list(map(int,input().split(" ")))
    lists={}
    for i in range(x[0]):
        lists[i]=list(map(int,input().split(" ")))
        lists[i].sort(reverse=True)

    num=0

    for i in range(x[0]):
        num = num+ lists[i][0] ** 2
    if num <x[1]:
        print(num)


