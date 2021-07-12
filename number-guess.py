import random
r = random.randint(1, 100)
count = 0
while True:
	n = input('請猜一個數字: ')
	n = int(n)
	count += 1
	if n < 1:
		print('數字為1到100的整數唷!')
	elif n > 100:
		print('數字為1到100的整數唷!')
	elif n == r:
		print('恭喜您猜對囉!')
		print('這是您猜的第', count, '次')
		break
	elif n < r:
		print('比您猜的數字還要大喔!')
	elif n > r:
		print('比您猜的數字還要小喔!')
	print('這是您猜的第', count, '次')