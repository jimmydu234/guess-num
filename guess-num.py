import random
num = random.randint(1, 100)
while True:
	ans = input('請猜一個1~100的數字:')
	ans  = int(ans)
	if ans == num:
		print('終於猜對了')
		break
	elif ans >= num:
		print('比答案大')
	elif ans < num:
		print('比答案小')		

