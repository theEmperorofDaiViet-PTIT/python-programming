'''Bài tập 1'''
class Person():
    def __init__(self, name, gender, date):
        self.name = name
        self.gender = gender
        self.date = date

    def description_person(self):
        full_info = f"{self.name} - {self.gender} - {self.date}"
        return full_info

class Student(Person):
    def __init__(self, name, gender, date, mssv, cpa, email):
        super().__init__(name, gender, date)
        self.mssv = mssv
        self.cpa = cpa
        self.email = email

    def description_student(self):
        full_info = self.description_person()
        full_info += f" - {self.mssv} - {self.cpa} - {self.email}"
        return full_info

    def check_schoolarship(self):
        if self.cpa >= 3.2:
            print("Eligible for scholarships")
        else:
            print("Not eligible for the scholarship")

student = Student("Nguyen Van A", "Nam", "01-01-2001","B1912345", 3.0, "nta@gmail.com")
print(student.description_student())
student.check_schoolarship()

'''Bài tập 2'''
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2*(self.height + self.width)

    def area(self):
        return self.height*self.width

rec = Rectangle(4, 6)
print(rec.area())
print(rec.perimeter())