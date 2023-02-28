import math
class Fraction:
	def __init__(self, son, mother):
		self.son = son
		self.mother = mother

	def rutgon(self):
		tmp = math.gcd(son, mother)
		self.son = self.son // tmp
		self.mother = self.mother // tmp

	def toString(self):
		print(f"{self.son}/{self.mother}")

son, mother = [int(x) for x in input().split()]
f = Fraction(son, mother)
f.rutgon()
f.toString()
