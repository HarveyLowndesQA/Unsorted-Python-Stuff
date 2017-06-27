salary = input("Enter your salary: ")
salary = int(salary)
grade = input("Enter your pay grade: ")
grade = int(grade)
dept = input("Enter your department: ")
CTO = input("Are you a CTO? (Y for yes, anything else for no): ")
isCTO = False
if(CTO == "Y"):
	isCTO = True

tax = 0;
bonus = 0;

if salary > 15000:
	if dept == "IT":
		if isCTO == False:
			if grade >= 1 and grade <= 10:
				tax = (salary * 0.09)
			elif grade >= 11 and grade <=20:
				tax = (salary * 0.15)
		bonus = salary * 0.05
	elif dept == "HR":
		if isCTO == False:
			if grade >= 1 and grade <= 10:
				tax = (salary * 0.09)
			elif grade >= 11 and grade <=20:
				tax = (salary * 0.17)
		else:
			tax = (salary * 0.09)

print("Your pre-tax salary is: £%d" %salary)
print("A total of £%.2f tax has been deducted from the wages." %tax)
print("Your total post-tax income is: £%.2f per annum" %(salary+bonus-tax))