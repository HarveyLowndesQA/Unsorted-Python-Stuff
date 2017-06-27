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

bonus = 1.05;

postTaxSalary = salary

if salary > 15000:
	if dept == "IT":
		if isCTO == False:
			if grade >= 1 and grade <= 10:
				postTaxSalary *= 0.91
			elif grade >= 11 and grade <=20:
				postTaxSalary *= 0.85
		postTaxSalary *= bonus; #bonus 5%
	elif dept == "HR":
		if isCTO == False:
			if grade >= 1 and grade <= 10:
				postTaxSalary *= 0.91
			elif grade >= 11 and grade <=20:
				postTaxSalary *= 0.83
		else:
			postTaxSalary *= 0.98

totalTaxPercentage = ((salary - postTaxSalary) / salary) * 100
print("Your pre-tax salary is: %d" %salary)
print("A total of %.2f percent has been deducted from your wages (this accounts for bonuses)" %totalTaxPercentage)
print("Your total post-tax income is: %d per annum" %postTaxSalary)