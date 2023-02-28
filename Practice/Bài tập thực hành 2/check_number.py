from math import sqrt
from prime import Prime
class CheckNumber(Prime):
    def __init__(self):
        pass

    def parity_check(self, x):
        if x %2 == 0:
            return True
        else: return False

    def is_prime(self, x):
        return super().is_prime(x)
    
    def is_perfect(self, x):
        s = 0
        for i in range(1, x):
            if x % i==0:
                s += i
        if s == x:
            return True
        else:
            return False

    def is_square(self, x):
        sq_root = int(sqrt(x))
        if (sq_root*sq_root) == x:
            return True
        else: return False


n = CheckNumber()
print(n.parity_check(8))
print(n.is_perfect(6))
print(n.is_prime(13))
print(n.is_square(9))