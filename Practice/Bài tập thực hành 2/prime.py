from math import sqrt
class Prime():
    def __init__(self):
        pass
    def is_prime(self, x):
        '''Function check number is prime or not'''
        if(x > 1):
            prime_flag = 0
            for i in range(2, int(sqrt(x)) + 1):
                if (x % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                return True
            else:
                return False
        else:
            return False

    def next_prime(self, x):
        if x<=1:
            return 2
        prime = x
        flag = True
        while(flag):
            prime += 1
            if self.is_prime(prime):
                flag = False
        return prime

# p = Prime()
# print(p.is_prime(18))
# print(p.next_prime(12))