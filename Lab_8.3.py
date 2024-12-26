"""  Lab 8 -----> Level 3

<<   List   >>

Level 2:
Ask the user to type 5 exam scores (0 – 100), and 5 names of students. Each name should have a corresponding score 
(e.g., the first grade is for the first student, and so on). Your program should:
Print the average score for the students.
Print the name of the student with the highest score. In case there is a tie return the last instance.

Level 3:
As a continuation from Level 2, include the following features:
Store the corresponding grade of each student, based on their score.
Print a record using a template (see below).
Print the name of the two students with the closest exam scores. 
Grades: U: 0 – 49, 3: 50 – 69, 4:70 – 84, 5: 85 - 100

Template:
Name: Max 16 characters, aligned to left. If more, cut it.
Exam Score: Occupy 10 characters. Scores are aligned to the right
Grade: Should occupy 5 characters, with numbers aligned to the right.
"""


def exams_reader():
    scores_list = []
    names_list = []

    for i in range(5):
        invalid_input = False
        while not invalid_input:
            try:
                score = int(input(f"Enter the score of the exam {i+1}: "))
                if 0 <= score <= 100:
                    scores_list.append(score)

                    name = input(f"Enter the name of the student {i+1}: ").capitalize()
                    names_list.append(name)
                    invalid_input = True
                else:
                    print("Invalid input! Enter a number between 0-100!")
        
            except ValueError:
                print("Enter only numbers!")                

    return scores_list, names_list


def calculation(scores, names):
    total_score = 0
    highest_score = scores[0]
    highest_index = 0

    for score in scores:
        total_score += score

    for i in range(len(scores)):
        if scores[i] > highest_score:
            highest_score = scores[i]
            highest_index = i

    avg_score = total_score / len(scores)

    return avg_score, highest_score, highest_index


def store_grades(scores):
    grades = []
    for score in scores:
        if 0 <= score <= 49:
            grades.append("U")
        elif 50 <= score <= 69:
            grades.append("3")
        elif 70 <= score <= 84:
            grades.append("4")
        elif 85 <= score <= 100:
            grades.append("5")

    return grades


def template():
    scores, names = exams_reader()
    avg_score, highest_score, highest_index = calculation(scores, names)
    grades = store_grades(scores)

    
    print(f"""-----------------------------------------
| Name             | Exam Score | Grade |
-----------------------------------------""")
    
    for i in range(len(names)):
        print(f"""| {names[i][:16]:<16} | {scores[i]:>10} | {grades[i]:>5} |
-----------------------------------------""")

    print(f"""| The average score is {avg_score}.            |
-----------------------------------------""")


def main():
    template()


if __name__ == "__main__":
    main()