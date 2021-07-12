height = input('請輸入您的身高(公尺): ')
weight = input('請輸入您的體重(公斤): ')
height = float(height)
weight = float(weight)
bmi = weight / height / height
bmi = float(bmi)
if bmi < 18.5:
	print('體重過輕', '你的BMI值為', bmi)
elif bmi >= 18.5 and bmi < 24:
	print('正常範圍', '你的BMI值為', bmi)
elif bmi >= 24 and bmi < 27:
	print('過重', '你的BMI值為', bmi)
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖' '你的BMI值為', bmi)
elif bmi >=30 and bmi < 35:
	print('中度肥胖', '你的BMI值為', bmi)
else:
	print('重度肥胖', '你的BMI值為', bmi)
