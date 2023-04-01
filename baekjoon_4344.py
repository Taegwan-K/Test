case_cnt = int(input())
total_grade = 0
up_cnt = 0
for cnt in range(0,case_cnt):
    student = input().split(' ')
    student_cnt = int(student[0])
    for x in range(1,student_cnt + 1):
        total_grade += int(student[x])
    avg = total_grade / student_cnt
    for y in range(1,student_cnt + 1):
        if float(student[y]) > avg:
            up_cnt += 1
    percent = float(up_cnt)*float(100)/float(student_cnt)
    print("%.3f%%"%percent)
    up_cnt = 0
    total_grade = 0