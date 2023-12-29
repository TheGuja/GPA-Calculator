from Grades import Grades


if __name__ == '__main__':
    input_response = ""
    grades = []

    while input_response.lower() != "q":
        input_response = input("Enter option from list below\n1) Enter Grades\n2) Display GPA\nQ) Quit\nResponse: ")

        if input_response == "1":
            print("Enter 'q' to finish.")
            continue_function = ""

            while continue_function.lower() != "n":
                course = input("Enter your course: ")
                grade_received = input("Enter your grade for the course: ")
                total_credits = input("Enter the number of credits for this course: ")
                grades.append(Grades(course, grade_received, total_credits))
                continue_function = input("Do you want to enter another course? (y/n) ")

        elif input_response == "2":
            current_credits_earned = 0.0
            credits_attempted = 0.0

            for grade in grades:
                current_credits_earned += grade.calculate_credits_earned()
                credits_attempted += float(grade.credits)

            print(current_credits_earned / credits_attempted)