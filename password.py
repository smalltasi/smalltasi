x = 3
while True:
	p = input('請輸入密碼: ')
	if p == 'a12345':
		print('登入成功')
		break
	else:
		print('密碼錯誤', '還剩', x, '次')
		x = x - 1
		if x < 1:
			break
