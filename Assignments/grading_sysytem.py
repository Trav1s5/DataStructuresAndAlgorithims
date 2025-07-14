#from itertools import count
from typing import List,Tuple


def show_history()->None:
    print("\n==Brief History of python==")
    print("\n ==Created in the year 1991==")
    print("\n == py 3 in the year 2008==")
    print("\n***Program that Computes the average score of students***")

def get_names_score() -> Tuple[List[str] , List[float]]: #names and scores
    while True:
        try:
            count = int(input("Number of Students:"))
            if count <=0:
                print("Please enter a number greater than zero")
                continue
            break
        except ValueError:
            print("Invalid input")

    names_of_students =[]
    scores=[]

    print("\n Enter student names and their scores: ")

    for i in range(count):
        name = input(f"student {i + 1} name:").strip()
        if not name:
            name = f"Student: {i+1}"
        names_of_students.append(name)

        while True:
            try:
                score = float(input(f"Enter the score for {name} :"))
                if 0 <= score <=100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100")

            except ValueError:
                print("Invalid Input.Please enter a numeric value: ")

    return names_of_students , scores

#grades score
def calculate_grades(scores: List[float])->List[str]:
    grades=[]
    for score in scores:
        if score>=70:
            grades.append("A")
        elif score >=60:
            grades.append("B")
        elif score >=50:
            grades.append("C")
        elif score >=40:
            grades.append("Pass")
        else:
            grades.append("Fail")
    return grades

#to display results
def display_results(names: List[str], scores: List[float],grades: List[str])->None:
    print("\n--- Student scores and Grades")
    for name, score ,grade in zip(names,scores,grades):
        print(f"{name}: Score= {score}, Grade={grade}")
    print("\nAverage score:", sum(scores) / len(scores))


# Main program execution
if __name__ == "__main__":
    show_history()
    names, scores = get_names_score()
    grades = calculate_grades(scores)
    display_results(names, scores,grades)


















