import datetime

class Gamer:
	def __init__(self, ID, name, start, end):
		self.ID = ID
		self.name = name
		self.start = start
		self.end = end
		self.hours = 0
		self.minutes = 0
		self.second = 0
		self.total = 0

	def calculate(self):
		sh, sm = [int(x) for x in self.start.split(':')]
		eh, em = [int(x) for x in self.end.split(':')]
		date = datetime.date(1, 1, 1)
		t1 = datetime.time(sh, sm)
		t2 = datetime.time(eh, em)
		T1 = datetime.datetime.combine(date, t1)
		T2 = datetime.datetime.combine(date, t2)
		d = T2 - T1
		s = str(d)
		self.hours, self.minutes, self.second = [int(x) for x in s.split(':')]
		self.total = self.hours * 60 + self.minutes		

	def toString(self):
		print(f"{self.ID} {self.name} {self.hours} gio {self.minutes} phut")

res = []
N = int(input())
for n in range(N):
	gamer = Gamer(input(), input(), input(), input())
	gamer.calculate()
	res.append(gamer)

res.sort(key = lambda k: -k.total)
for mem in res:
	mem.toString()