class Grades:
    def __init__(self, course = None, grade = None, credits = None, scale = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0}):
        self.course = course
        self.grade = grade
        self.credits = credits
        self.scale = scale

    def calculate_credits_earned(self):
        return float(self.credits) * self.scale[self.grade]

if __name__ == "__main__":
    grades = []
    grades.append(Grades("Calc 3", "B+", 4))
    print(grades[0].course)