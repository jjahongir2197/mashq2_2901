class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0

    def study(self, percent):
        self.progress += percent
        if self.progress > 100:
            self.progress = 100


class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def show(self):
        for s in self.students:
            print(f"{s.name} | Progress: {s.progress}%")


course = Course("Python OOP")

while True:
    print("\n1.Talaba 2.O‘qish 3.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        course.enroll(Student(input("Ism: ")))
    elif c == "2":
        i = int(input("Index: "))
        course.students[i].study(int(input("Foiz: ")))
    elif c == "3":
        course.show()
    elif c == "0":
        break
