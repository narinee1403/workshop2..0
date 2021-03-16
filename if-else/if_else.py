point = int(input("Enter you score : "))
grade = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
score = [80, 75, 70, 65, 60, 55, 50, 0]
z = 0
for y in grade:
    if point >= score[z]:
        print("Grade : " + grade[z])
        break
    z = z + 1
