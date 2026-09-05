def calculate_grade (average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
def get_valid_score(subject):
    while True:
        score = float(input(f"Enter {subject} score: "))
        if 0 <= score <= 100:
            return score
        print("Invalid score.")
        print("please enter a valid score between 0 and 100.")
    
def add_student(students):
    name = input("Enter student name: ")
    math_score = get_valid_score("Math")
    english_score = get_valid_score("English")
    science_score = get_valid_score("Science")
    students.append([name, math_score, english_score, science_score])
    print("Student added successfully.")

def view_all_students(students):
    print("=== ALL STUDENTS ===")
    

    if len(students) == 0:
        print("No student found. ")
        return
    
    for index , student in enumerate(students):
        name = student[0]
        total = student[1] + student[2] + student[3]
        average = total / 3
        grade = calculate_grade(average) 

        print(f"{index + 1}. {name}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")

def search_student(students):
    search_name = input("Enter student name to search: ")

    for student in students:
        if student[0].lower() == search_name.lower():
            name = student[0]
            math_score = student[1]
            english_score = student[2]
            science_score = student[3]
            total = math_score + english_score + science_score
            average = total / 3
            grade = calculate_grade(average)

            print("=== STUDENT FOUND ===")
            print(f"Name: {name}")
            print(f"Mathematics: {math_score:.0f}")
            print(f"English: {english_score:.0f}")
            print(f"Science: {science_score:.0f}")
            print(f"Total: {total:.0f}")
            print(f"Average: {average:.2f}")
            print(f"Grade: {grade}")
            return
    print()
    print("Student not found. ")   

def find_top_student(students):
    if len(students) == 0:
        print("No student found. ")
        return
    
    top_name = ""
    top_average = -1
    top_grade = ""
    
    for student in students:
        total = student[1] + student[2] + student[3]
        average = total / 3 
        grade = calculate_grade(average)

        if average > top_average:
            top_average = average
            top_name = student[0]
            top_grade = grade 
    print("=== TOP STUDENT ===")
    print(f"Name: {top_name}")
    print(f"Average: {top_average:.2f}")
    print(f"Grade: {top_grade}")

def class_statistics(students):
    print("=== CLASS STATISTICS ===")

    if len(students) == 0:
        print("No student found. ")
        return
    total_of_average = 0
    for student in students:
        total = student[1] + student[2] + student[3]
        average = total / 3
        total_of_average += average
        class_average = total_of_average / len(students)

        print(f"Number of students: {len(students)}")
        print(f"Class average: {class_average:.2f}")
        print() 

def remove_student(students):
    remove_name = input("Enter student name to remove: ")

    for student in students:
        if student[0].lower() == remove_name.lower():
            students.remove(student)
            print(f"{student[0]} has been removed successfully. ")
            return
    print("student not found.")

def update_student(students):
    update_name = input("Enter student name to update: ")

    for student in students: 
        if student[0].lower() == update_name.lower():
            print()
            student[1] = get_valid_score("new Mathematics")
            student[2] = get_valid_score("new English")
            student[3] = get_valid_score("new Science")

            print("Student information updated sucessfully.")
            return
    print("Student not found. ")

def main(): 
    students = []
    running = True

    while running:
        print("=== STUDENT MANAGEMENT SYSTEM===")
        print("1. Add student")
        print("2. View All Students")
        print("3. Search for students") 
        print("4. Find top student")
        print("5. Class statistics")
        print("6. Remove students")
        print("7. Update student information")
        print("8. Exit")

        choice = input("Enter your choice (1-8):")
        print()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            find_top_student(students)
        elif choice == "5":
            class_statistics(students)
        elif choice == "6":
            remove_student(students)
        elif choice == "7":
            update_student(students)
        elif choice == "8":
            running = False
            print("Thank You For Using The Student Management System.")
            print(" Goodbye:-)")
        else:
            print("Invalid choice. Please try again.")
            
main() 

          
            