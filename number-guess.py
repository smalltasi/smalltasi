import random
r = random.randint(1, 100)
count = 0
while True:
	n = input('請猜一個數字: ')
	n = int(n)
	count += 1
	if r == n:
		print('恭喜您猜對囉!')
		print('這是您猜的第', count, '次')
		break
	elif r < n:
		print('比您猜的數字還要小喔!')
	elif r > n:
		print('比您猜的數字還要大喔!')
	elif n < 1 and n >100:
		print('數字為1到100的整數唷!')
	print('這是您猜的第', count, '次')