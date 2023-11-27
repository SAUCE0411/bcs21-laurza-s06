# Initialize an empty list to store student data
student_data = []

# Function to compute the final grade and equivalent
def compute_grade(q1, q2, q3, cp, final_exam):
    q_total = (q1 + q2 + q3) / 3
    grade = q_total * 0.4 + cp * 0.1 + final_exam * 0.5
    equivalent = "Passed" if grade > 75 else "Failed"
    return grade, equivalent

# Input loop
print("\n********** GRADING SYSTEM **********")
while True:
    name = input("\nEnter student name: ")
    q1 = float(input("Enter grade for Quiz 1: "))
    q2 = float(input("Enter grade for Quiz 2: "))
    q3 = float(input("Enter grade for Quiz 3: "))
    cp = float(input("Enter grade for Class Participation: "))
    final_exam = float(input("Enter grade for Final Exam: "))
    
    # Compute final grade and equivalent
    grade, equivalent = compute_grade(q1, q2, q3, cp, final_exam)
    
    # Add student data to the list
    student_data.append([name, q1, q2, q3, cp, final_exam, grade, equivalent])
    
    add_more = input("\nDo you want to add more students? (Yes/No): ").strip().lower()
    if add_more != "yes":
        break

# Display the student data
print(" |--------------------------------|----------|---------|---------|---------|---------------|----------|---------------|")
print(" |               NAME             |    Q1    |    Q2   |    Q3   |    CP   |   FINAL EXAM  |   GRADE  |   EQUIVALENT  |")
print(" |--------------------------------|----------|---------|---------|---------|---------------|----------|---------------|")
for student in student_data:
    print(f" |  {student[0]:<16}              |  {student[1]:<7.2f} | {student[2]:<7.2f} | {student[3]:<7.2f} | {student[4]:<7.2f} | {student[5]:<13.2f} | {student[6]:<8.2f} | {student[7]:<13} |")
print(" |--------------------------------|----------|---------|---------|---------|---------------|----------|---------------|")

# Calculate and display the total number of students passed and failed
passed_count = 0
failed_count = 0

for student in student_data:
    if student[7] == "Passed":
        passed_count += 1
    elif student[7] == "Failed":
        failed_count += 1

print(f"\nTotal no. of Students Passed: {passed_count}")
print(f"Total no. of Students Failed: {failed_count}")

