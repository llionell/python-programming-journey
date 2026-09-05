def calculate_grade (average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "c"
    elif average >= 60:
        return "D"
    else:
        return "F"

num_students = int(input( "How many students?" ))
students = []
for i in range(num_students):
    print()
    name= input(f"Enter student { i + 1} name: ")
    math_score = float(input( "Enter Mathematics score: "))
    english_score= float(input("Enter English score: "))
    science_score= float(input("Enter Science score: "))
    students.append ([name, math_score, english_score, science_score ])

top_name = ""
top_average = -1
top_grade = ""
    
for student in students:
    name= student[0]
    math_score = student[1]
    english_score = student[2]
    science_score = student[3]
    total = math_score + english_score + science_score
    average = total / 3
    grade = calculate_grade(average)

    print(name)
    print(f"average: {average:.2f}")
    print(f"Grade: {grade}")

    

    if average > top_average: 
        top_average = average
        top_name = name
        top_grade = grade 
print(f"Name: {top_name}")
print(f"Average: {top_average}")
print(f"Grade: {top_grade}")

    