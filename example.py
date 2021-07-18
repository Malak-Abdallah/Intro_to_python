# from collections import Counter, OrderedDict

# another practical solution:
# class OrderedCounter(Counter, OrderedDict):
#    pass
# [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]

if __name__ == '__main__':
    s = input()
    acc = {}
    for c in s:
        if c in acc:
            acc[c] = int(acc[c]) + int(1)
        else:
            acc[c] = int(1)

    sort_orders = dict(sorted(acc.items(), key=lambda x: x[1], reverse=True))
    flipped = {}

    for key, value in sort_orders.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)

    for key, value in list(flipped.items()):
        if len(value) > 1:
            k = key
            v = list(value)
            del flipped[key]
            v.sort()
            flipped[k] = v

    j = 0
    for key, value in flipped.items():
        for i in range(len(list(value))):
            if j == 3:
                break
            else:
                print(value[i], key)
                j = j + 1
