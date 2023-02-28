class Staff():
	def __init__(self, income, LCB):
		self.income = int(income)
		self.LCB = int(LCB)
		self.LT = self.income - self.LCB
		self.real = 0

		self.BHXH = self.LCB * 0.08
		self.BHYT = self.LCB * 0.015
		self.BHTN = self.LCB * 0.01
		self.BH = self.BHXH + self.BHYT + self.BHTN
		self.DP = self.LCB * 0.01

		self.CKGT = 11000000
		self.rate = 0
		self.tax = 0

		self.TNCT = self.income - self.CKGT - self.BH

	def calTax(self):
		if self.TNCT > 80000000:
			self.rate = 0.35
			self.taxt = self.TNCT * self.rate - 9850000
		elif self.TNCT > 52000000:
			self.rate = 0.30
			self.taxt = self.TNCT * self.rate - 5850000
		elif self.TNCT > 32000000:
			self.rate = 0.25
			self.taxt = self.TNCT * self.rate - 3250000
		elif self.TNCT > 18000000:
			self.rate = 0.20
			self.taxt = self.TNCT * self.rate - 1650000
		elif self.TNCT > 10000000:
			self.rate = 0.15
			self.taxt = self.TNCT * self.rate - 750000
		elif self.TNCT > 5000000:
			self.rate = 0.10
			self.taxt = self.TNCT * self.rate - 250000
		elif self.TNCT == 5000000:
			self.rate = 0.05
			self.taxt = self.TNCT * self.rate

	def calReal(self):
		self.calTax()
		self.real = self.income - (self.BH + self.DP + self.tax)


	def toString(self):
		if self.income < 1000 or self.LCB < 1000:
			print("INVALID INPUT")
		else:
			print(int(self.real))

def __main__():
	N = int(input())
	if N > 10 or N < 0:
		print("INVALID INPUT")
	else:
		for test in range(N):
			data = list(map(int, input().split()))
			a = data[0]
			b = data[1]
			s = Staff(a, b)
			s.calTax()
			s.calReal()
			s.toString()

__main__()