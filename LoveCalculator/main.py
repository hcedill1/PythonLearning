print("Welcome to the love Calculator\n")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

count1 = name1.lower().count("t")
count1 = count1 + name1.lower().count("r")
count1 = count1 + name1.lower().count("u")
count1 = count1 + name1.lower().count("e")

count1 = count1 + name2.lower().count("t")
count1 = count1 + name2.lower().count("r")
count1 = count1 + name2.lower().count("u")
count1 = count1 + name2.lower().count("e")

count2 = name1.lower().count("l")
count2 = count2 + name1.lower().count("o")
count2 = count2 + name1.lower().count("v")
count2 = count2 + name1.lower().count("e")

count2 = count2 + name2.lower().count("l")
count2 = count2 + name2.lower().count("o")
count2 = count2 + name2.lower().count("v")
count2 = count2 + name2.lower().count("e")

score = int(str(count1) + str(count2))

if(score < 10 & score > 90):
    print(f"Your score is {score}, you go together like coke and menthos")
elif(score > 40 & score < 50):
    print(f"Your score is {score}, you are alright togther")
else:
    print(f"Your score is {score}")