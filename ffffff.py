class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self, hours):
        self.grade += hours * 0.1

    def play(self, hours):
        self.grade -= hours * 0.05

    def get_grade(self):
        return self.grade

student = Student( "Зоряна", 8)

lesson = float(input("Навчіть студента - "))
student.study(lesson)

game = float(input("ПОграйте з студентом - "))
student.play(game)

grade = student.get_grade()

print(f"Оцінка студента {student.name}: {grade}")



