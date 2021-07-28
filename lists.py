# TASK 1:
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. '
# 'You are given  scores. Store them in a list and find the score of the runner-up.


# TASK 2:
# Given the names and grades for each student in a class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a new line.


if __name__ == '__main__':
    num = int(input("enter task number"))
    if num == 1:
        n = int(input())
        arr = map(int, input().split())
        print(sorted(list(set(arr)))[-2])
    else:
        marks = {}
        result = []
        for _ in range(int(input())):
            name = input()
            score = float(input())
            marks[name] = score
        second = sorted(list(set(marks.values())))[1]  # we got the second lowest mark
        for key, value in marks.items():
            if value == float(second):
                result.append(key)
        # for the alphabetical order:
        result.sort()
        for i in result:
            print(i)

