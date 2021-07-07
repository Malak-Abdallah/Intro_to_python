# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided.

if __name__ == '__main__':
    n = int(input("Enter number of students"))
    student_marks = {}
    sum=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter student name to get its score avg ")
    for i in student_marks[query_name]:
        sum=float(sum+float(i))

    print(str(sum/len(student_marks[query_name])))