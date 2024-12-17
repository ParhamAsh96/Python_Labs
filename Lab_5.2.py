"""
<<   For Loops   >>

• Write a program that asks the user to enter the number of
students.
• Then it asks for each student's name and score.
• Finally, it will display the name of the student with the highest
score.
"""

student_list = []
score_list = []

students_count = int(input("How many students attended the exam? "))

for i in range(students_count):
    name = input("\nEnter the name of the student: ")
    student_list.append(name)
    score = float(input("Enter student's score: "))
    score_list.append(score)

highest_index = 0
for i in range(1, len(score_list)):
    if score_list[highest_index] < score_list[i]:
        highest_index = i
    
print(f"\n{student_list[highest_index].capitalize()} achieved highest score with {score_list[highest_index]}.\n")