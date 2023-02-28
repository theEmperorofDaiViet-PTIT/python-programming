class Student:
	def __init__(self, ID, name, team):
		self.ID = ID
		self.name = name
		self.team = team
		self.record = ""
		self.score = 10
		self.result = ""

	def calculate(self):
		for char in self.record:
			if char == 'm':
				self.score -= 1
			elif char == 'v':
				self.score -= 2

	def decision(self):
		if self.score <= 0:
			self.result = "0 KDDK"
		else:
			self.result = str(self.score)

	def toString(self):
		print(f"{self.ID} {self.name} {self.team} {self.result}")


N = int(input())
dssv = []
for n in range(N):
	stu = Student(input(), input(), input())
	dssv.append(stu)

for n in range(N):
	stuID, record = [s for s in input().split()]
	for mem in dssv:
		if mem.ID == stuID:
			mem.record = record
			mem.calculate()
			mem.decision()

for mem in dssv:
	mem.toString()