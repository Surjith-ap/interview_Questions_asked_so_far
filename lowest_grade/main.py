if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input().strip()
        score = float(input().strip())
        students.append([name, score])
    student_dict = dict(students)
    name_list = list(student_dict.keys())
    score_list = list(student_dict.values())
    
    first = second = float('inf')
    for i in score_list:
        if i < first:
            second = first
            first = i
        elif i < second and i != first:
            second = i
    if second == float('inf'):       
        print(None)
    else:
        second_least = second
    for key, value in sorted(student_dict.items()):
        if value == second_least:
            print(key)
