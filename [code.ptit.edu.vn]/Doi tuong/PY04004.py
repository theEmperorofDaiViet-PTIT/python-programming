import math
class Fraction:
	def __init__(self, son, mother):
		self.son = son
		self.mother = mother

	def rutgon(self):
		tmp = math.gcd(self.son, self.mother)
		self.son = self.son // tmp
		self.mother = self.mother // tmp

	def plus(self, f):
		self.son = self.son * f.mother + self.mother * f.son
		self.mother = self.mother * f.mother
		self.rutgon()

	def toString(self):
		print(f"{self.son}/{self.mother}")

son1, mother1, son2, mother2 = [int(x) for x in input().split()]
f1 = Fraction(son1, mother1)
f2 = Fraction(son2, mother2)
f1.plus(f2)
f1.toString()