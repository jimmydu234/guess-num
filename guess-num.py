import random
num = random.randint(1, 100)
count = 0
while True:
	count += 1
	ans = input('請猜一個1~100的數字:')
	ans  = int(ans)
	if ans == num:
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	elif ans >= num:
		print('比答案大')
	elif ans < num:
		print('比答案小')
	print('這是你猜的第', count, '次')			

