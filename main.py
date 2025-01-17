# プログラムの説明:
# このプログラムは、複数の学生の成績を管理し、合計点と平均点を計算し、
# 最も成績の良い学生を見つけます。
def run(students):
    print_score(students)
    y, x = find_top(students)
    return y, x

def print_score(students):
    for s in students:
        total = 0
        count = 0
        for g in students[s]:
            total += g
            count += 1
        avg = total / count
        print(f"Student: {s}, Total: {total}, Average: {avg}")

def find_top(students):
    x = 0
    y = ""
    for s in students:
        total = 0
        count = 0
        for g in students[s]:
            total += g
            count += 1
        if total > x:
            x = total
            y = s
    return y, x

students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [70, 75, 80],
    "David": [95, 85, 90]
}

top_student, top_score = run(students)
print(f"Best student: {top_student} with total score: {top_score}")