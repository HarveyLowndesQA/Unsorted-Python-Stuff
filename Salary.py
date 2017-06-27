salary = input("Enter your salary: ")
salary = int(salary)

grade = input("Enter your pay grade: ")
grade = int(grade)

dept = input("Enter your department: ")

CTO = input("Are you a CTO? (Y for yes, anything else for no): ")
if(CTO == "Y"):
	isCTO = True
else:
	isCTO = False

tax = 0;
bonus = 1;

if salary > 15000:
	if dept == "IT":
		if isCTO == False:
			if grade >= 1 and grade <= 10:
				tax = 9
			elif grade >= 11 and grade <=20:
				tax = 15
		bonus = 1.05; #5%
	elif dept == "HR":
		if isCTO == False:
			if grade >= 1 and grade <= 10:
				tax = 9
			elif grade >= 11 and grade <=20:
				tax = 17
		else:
			tax = 2

tax = (100 - tax) / 100;
postTaxSalary = (salary * tax) * bonus;
totalTaxPercentage = ((salary - postTaxSalary) / salary) * 100
print("Your pre-tax salary is: %d" %salary)
print("A total of %.2f percent has been deducted from your wages (this accounts for bonuses)" %totalTaxPercentage)
print("Your total post-tax income is: %d per annum" %postTaxSalary)