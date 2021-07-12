import time
ans = 'Y'
while ans == 'Y':
	import random
	start = input('請輸入遊戲最小數值: ')
	end = input('請輸入遊戲最大數值: ')
	start = int(start)
	end = int(end)
	r = random.randint(start, end)
	while True:
		n = input('請猜一個數字: ')
		n = int(n)
		if n > end:
			print('是', start, '到', end, '的整數唷!')
		elif n < start:
			print('是', start, '到', end, '的整數唷!')
		elif n == r:
			print('恭喜你答對了!')
			break
		elif n > r:
			print('比您的數字小')
		elif n < r:
			print('比您的數字大')
	ans = input('是否繼續遊戲(Y/N): ')
print('謝謝您的遊玩')
time.sleep(3)