# weight = float(input("enter your weight in kg: "))
# height = float(input("enter your height in m: "))


# bmi = round((weight / (pow(height,2))))

# print(bmi)

# if bmi < 18.5:
#     print("You are underweight")
# elif bmi < 25:
#     print("You are normal weight")
# elif bmi < 30:
#     print("You are overweight")
# elif bmi < 35: 
#     print("You are obese")
# else: 
#     print("You are clinically obese")

#Leap year challange

year = int(input("Which year do you want to check? "))

checkDivFour = year % 4
checkDivHundred = year % 100
checkDivFourHund = year % 400


if (checkDivFour == 0 & checkDivHundred != 0) | checkDivFourHund == 0:
    print("Leap year")
    
else: 
    print("No Leap Year")