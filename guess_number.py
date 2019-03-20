import random
r = random.randint(1,100)

while True:
	
	guess = input("輸入數字: ")
	guess = int(guess)
	if guess == r:
		print("終於猜對了")
		break
	elif guess > r:
		print("比答案大")
	else:
		print("比答案小")
print(count)
