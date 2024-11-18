from pluggy import Result
student_grades = {"course1": "100"}

while True:
    print("\n1. Adding grades")
    print("2. Updating grades")
    print("4. Viewing grades")
    print("4. Exit")
    
    choice = input("Select your option to proceed: ")
    
    if choice == "1":
        student_grades[input{"Enter Course name: "} = int(input{"Enter Grade: "})]
    if choice == "2":
        student_grades[input{"Enter the course name again:"} = int(input{"Enter New Grade: "})]
    if choice == "3":
        student_grades[input{""}]





for key, value in student_grades.items():
    print(f"{key}: {value}")