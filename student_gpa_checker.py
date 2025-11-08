# David Cruz
# student_gpa_checker.py
# This app accepts student names and GPAs, and checks if they qualify for the Dean's List or Honor Roll.
# The program continues until the user enters 'ZZZ' as the last name.

while True:
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
    if last_name.upper() == 'ZZZ':
        print("Exiting program. Goodbye!")
        break

    first_name = input("Enter student's first name: ")
    
    try:
        gpa = float(input("Enter student's GPA: "))
    except ValueError:
        print("Invalid GPA. Please enter a numeric value.")
        continue

    print(f"\nStudent: {first_name} {last_name}")
    
    if gpa >= 3.5:
        print("Congratulations! You've made the Dean's List.")
    elif gpa >= 3.25:
        print("Great job! You've made the Honor Roll.")
    else:
        print("Keep working hard! You can do it.")

    print("-" * 40)
