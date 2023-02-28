from datetime import date

def solve(d):
	if date(2020, 3, 21) <= d and d <= date(2020, 4, 19):
		return "BACH DUONG"
	if date(2020, 4, 20) <= d and d <= date(2020, 5, 20):
		return "KIM NGUU"
	if date(2020, 5, 21) <= d and d <= date(2020, 6, 20):
		return "SONG TU"
	if date(2020, 6, 21) <= d and d <= date(2020, 7, 22):
		return "CU GIAI"
	if date(2020, 7, 23) <= d and d <= date(2020, 8, 22):
		return "SU TU"
	if date(2020, 8, 23) <= d and d <= date(2020, 9, 22):
		return "XU NU"
	if date(2020, 9, 23) <= d and d <= date(2020, 10, 22):
		return "THIEN BINH"
	if date(2020, 10, 23) <= d and d <= date(2020, 11, 22):
		return "THIEN YET"
	if date(2020, 11, 23) <= d and d <= date(2020, 12, 21):
		return "NHAN MA"
	if date(2020, 12, 22) <= d or d <= date(2020, 1, 19):
		return "MA KET"
	if date(2020, 1, 20) <= d and d <= date(2020, 2, 18):
		return "BAO BINH"
	if date(2020, 2, 19) <= d and d <= date(2020, 3, 20):
		return "SONG NGU"
	else:
		return ""

t = int(input())
for test in range(t):
	d, m = [int(x) for x in input().split()]
	print(solve(date(2020, m, d)).title())