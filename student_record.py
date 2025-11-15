import  math
import sys

Studyante =  []
clubs = {"Python Class", "Java Expert", "Full-Stack Programming"}

def Menu():
    print("\n ---------- STUDENT RECORD -----------")
    print("1. View All Students")
    print("2. Add Student")
    print("3. Manage Clubs")
    print("4. Show Grade Statistics")
    print("5. Exit System")

def add_student():
    print("\n ---------- ADD STUDENT RECORD -----------")
    name = input("Enter Student Name: ")
    while True:
        try:
            age = int(input("Enter Age: "))
            if age <=0:
                print("Age must be positive.")
            else:
                break
        except ValueError:
            print("Invalid Input, please try again.")

    course = input("Enter Course: ")

    grade_record = []
    print("Enter Student Grade: ")
    for i in range(1,4):
        while True:
            try:
                grade = float(input(f"Enter Grade {i} (0-100): "))
                if grade >= 0 and grade <= 100:
                    grade_record.append(grade)
                    break
                else:
                    print("Error!!Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid Input, please try again.")

    grade_tuple = tuple(grade_record)
    student_record = {
        "Name" : name,
        "Age" : age,
        "Course" : course,
        "Grades" : grade_tuple,
    }

    Studyante.append(student_record)
    print(f"\n Student '{name}' added successfully!")

def view_all_students():
    print("\n 1. ---------- VIEW STUDENT RECORD -----------")
    if not Studyante:
        print("No record found.")
        return

    print(f"{'No.':<4}{'Name':<20}{'Age':<5}{'Course':<15}{'Grades':<20}")
    print("-" *64)

    for i, student in enumerate(Studyante,1):
        grade_string = ", ".join(map(str, student['Grades']))
        print(f"{i:<4}{student['Name']:<20}{student['Age']:<5}{student['Course']:<15}{grade_string:<20}")
    print("_"*64)

def analyze_grade():
    print("\n 4. ---------- ANALYZE STUDENT RECORD -----------")
    if not add_student:
        print("No Student record to analyze dol.")
        return
    name_find = input("Enter students name to analyze: ")
    found_student = None
    for student in Studyante:
        if student['Name'].lower() == name_find.lower():
            found_student = student
            break

    if found_student:
        grades = found_student['Grades']
        print(f"\nStatistics for: {found_student['Name']} (Grades: {grades})")

        highest_grade = max(grades)
        print(f"* Highest Grade: **{highest_grade}**")

        lowest_grade = min(grades)
        print(f"* Lowest Grade: **{lowest_grade}**")

        total_sum = sum(grades)
        count = len(grades)
        average_grade = total_sum / count
        grade_final = math.floor(average_grade)
        print(f"* Average Grade: {average_grade}")
    else:
        print(f"Student '{name_find}' not found.")

def manage_clubs():
    while True:
        print("\n--- 3. Manage Clubs Menu ---")
        print("1. Add a Club")
        print("2. View All Clubs")
        print("3. Remove a Club")
        print("4. Back to Main Menu")
        club_choice = input("Enter your choice (1-4): ")

        if club_choice == "1":
            new_club = input("\n--- Enter Club Name ---: ")
            in_size = len(clubs)
            clubs.add(new_club)
            if len(clubs) > in_size:
                print(f" Club '{new_club}' added.")
            else:
                print(f" Club '{new_club}' was already registered.")


        elif club_choice == '2':
            print("\n--- Registered Clubs (Set) ---")
            if clubs:
                for club in sorted(clubs):
                    print(f"- {club}")
            else:
                print("No clubs registered yet.")

        elif club_choice == '3':
            club_to_remove = input("Enter the name of the club to remove: ")
            try:
                clubs.remove(club_to_remove)
                print(f" Club '{club_to_remove}' removed.")
            except KeyError:
                print(f" Error: Club '{club_to_remove}' not found.")

        elif club_choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
def main():
    while True:
        Menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            view_all_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            manage_clubs()
        elif choice == "4":
            analyze_grade()
        elif choice == "5":
            print("Thank you for using this program, Goodbye.!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()







