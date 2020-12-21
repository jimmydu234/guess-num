import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

num = random.randint(start, end)
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

