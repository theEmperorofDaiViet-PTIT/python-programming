class Student:
	def __init__(self, name, dob, score1, score2, score3):
		self.name = name
		self.dob = dob
		self.score1 = score1
		self.score2 = score2
		self.score3 = score3
		self.total = score1 + score2 + score3

	def toString(self):
		print(f"{self.name} {self.dob}", end = ' ')
		print("%.1f" % self.total)

name = input()
dob = input()
score1 = float(input())
score2 = float(input())
score3 = float(input())
s = Student(name, dob, score1, score2, score3)
s.toString()