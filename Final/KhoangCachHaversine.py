import math

long1, lat1 = [float(x) for x in input().split()]
long2, lat2 = [float(x) for x in input().split()]

deltalat = lat2 - lat1
deltalong = long2 - long1

R = 6371

a = math.pow(math.sin(deltalat / 2), 2) + math.cos(lat1) * math.cos(lat2) * math.pow(math.sin(deltalong / 2), 2)
c = 2 * math.asin(math.sqrt(a))
d = R * c
print("%.2f" % d)
