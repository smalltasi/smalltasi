passward = 'a12345'
x = 3
while x > 0:
	p = input('請輸入密碼: ')
	if p == passward:
		print('登入成功!')
		break
	else:
		print('密碼錯誤', '剩', x, '次')
		x = x - 1
		if x < 1 :
			print('登入失敗', '帳號鎖定')