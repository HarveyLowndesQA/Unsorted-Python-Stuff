
no1 = input("Enter a number: ")
x = int(no1)

if x > 100:
	print("a")
	if x > 500:
		print("1")
	else:
		print("2")
else:
	print("b")
	if(x < 50):
		print("4")
	else:
		print("3")