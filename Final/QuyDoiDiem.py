class Student:
	def __init__(self, name, cc, kt, btl, thi):
		self.name = name
		self.cc = float(cc)
		self.kt = float(kt)
		self.btl = float(btl)
		self.thi = float(thi)
		self.result = ""
		self.tier = ""

	def calculateTotal(self):
		score = self.cc * 0.1 + self.kt * 0.1 + self.btl * 0.2 + self.thi * 0.6
		if score >= 8.5:
			self.result = 'A'
			self.tier = 'Giỏi'
		elif score >= 7.0:
			self.result = 'B'
			self.tier = 'Khá'
		elif score >= 5.5:
			self.result = 'C'
			self.tier = 'Trung bình'
		elif score >= 4.0:
			self.result = 'D'
			self.tier = 'Trung bình kém'
		else:
			self.result = 'F'
			self.tier = 'Kém'

	def toString(self):
		print(self.name)
		print(self.result)
		print(self.tier)


s = Student(input(), input(), input(), input(), input())
s.calculateTotal()
s.toString()