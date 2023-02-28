n = int(input())
dssv = []
for t in range(n):
    sv = {}
    sv['Name'] = input()
    sv['AC'], sv['Submit'] = [int(x) for x in input().split()]
    dssv.append(sv)

dssv = sorted(dssv, key = lambda k: (-k['AC'], k['Submit'], k['Name']))
for mem in dssv:
    print(*mem.values())