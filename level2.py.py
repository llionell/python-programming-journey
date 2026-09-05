def calculate_grade (average):
    if average >= 90:
        grade ="A"
    elif average >= 80:
        grade ="B"
    elif average >= 70:
        grade ="c"
    elif average >= 60:
        grade ="D"
    else:
        grade ="F"

num_students = int(input( "How many students?" ))
students = []
for i in range(num_students):
    print()
    name= input(f"Enter student { i + 1} name: ")
    math_score = float(input( "Enter Mathematics score: "))
    english_score= float(input("Enter English score: "))
    science_score= float(input("Enter Science score: "))
    students.append ([name, math_score, english_score, science_score ])
    
for student in students:
    name= student[0]
    math_score = student[1]
    english_score = student[2]
    science_score = student[3]
    total = math_score + english_score + science_score
    average = total / 3
    grade = calculate_grade(average)

    print(name)
    print(f"Total: {total:.0f}")
    print(f"average: {average:.2f}")
    print(f"Grade: {grade}")

    

