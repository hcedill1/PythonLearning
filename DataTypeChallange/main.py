#Write a program that adds the digits in a 2 digit number.
#If the input was 35, the the output should be 3 + 5 = 8

# user_input = input("Enter a 2 digit number:\n")
# firstNum = int(user_input[0])
# secNum = int(user_input[1])

# sum = firstNum + secNum;

# print(type(sum))

# print("\nResult: " + str(sum))


#This is a nother coding challange that get the BMI calculation 
#from the what the user inputs.

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# print(type(height))
# print(type(weight))

# BMI= (int(weight) / (float(height) ** 2))

# print(int(BMI))

#Another coding challange Life in Weeks
#1 year = 365 days 
#1 year = 52 weeks 
#1 year = 12 months 

# ageInput = input("What is your current age?\n")
# lifeAgeDays = 90 * 365
# lifeAgeWeeks = 90 * 52
# lifeAgeMonths = 90 * 12

# difDays = lifeAgeDays - (int(ageInput) * 365)
# difWeeks = lifeAgeWeeks - (int(ageInput) * 52)
# difMonths = lifeAgeMonths - (int(ageInput) * 12)

# print(f"You have {difDays} days, {difWeeks} weeks, and {difMonths} months left")

#Tip Calculator Challange 

print("Welcome to the tip calculator.\n")
total_bill = input("What is the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
split_bill = input("How many people to split the bill? ")
convert_perc = float(percentage)/100
perc_bill_total = float(total_bill) * convert_perc
total_with_grat = float(total_bill) + perc_bill_total
split = total_with_grat/float(split_bill)
print(f"Each person should pay: ${round(split,2)}")







