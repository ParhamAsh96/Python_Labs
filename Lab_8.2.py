"""  Lab 8 -----> Level 2

<<   List   >>

Ask the user to type 5 exam scores (0 – 100), and 5 names of students. Each name should have a corresponding score 
(e.g., the first grade is for the first student, and so on). Your program should:
Print the average score for the students.
Print the name of the student with the highest score. In case there is a tie return the last instance.
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


def calculation():
    scores, names = exams_reader()

    total_score = 0
    highest_score = scores[0]
    highest_index = 0

    for  score in scores:
        total_score += score

    for i in range(len(scores)):
        if scores[i] > highest_score:
            highest_score = scores[i]
            highest_index = i

    avg_score = total_score / len(scores)

    return names, avg_score, highest_score, highest_index


def main():
    names, average_score, highest_score, highest_index = calculation()

    print(f"\nThe average score for students is {average_score}.")
    print(f"{names[highest_index]} got the highest score, {highest_score}.\n")


if __name__ == "__main__":
    main()