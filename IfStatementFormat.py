#IfStatementFormat

no1 = input("Enter first number: ")
no2 = input("Enter second number: ")

x = int(no1)
y = int(no2)
z = x + y
pas = 10;

print("%d + %d = %d" %(x, y, z))

if z>pas:
	print("%d is a pass" %z)
else:
	print("%d is a fail" %z)
