#Simple Project 3
# CONTROL FLOW & LOGICAL OPERATORS
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What's your age?"))
    if age < 12:
        bill += 5
        print("childs ticket are $5.")
    elif age <= 18:
        bill += 7
        print("Youth ticket are $7.")
    elif age >= 45 and age <= 55:
        bill += 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill += 12
        print("Adult ticket are $12")
    wants_photo = (input('Do you want a photo taken? "Y" or "N" \n')).upper()
    if wants_photo == "Y":
        bill += 3
        print(f"Please pay ${bill}")
    else:
        bill += 0
        print("you don't need to pay anything. Have fun!")
        
else:
    print("You can't ride the rollercoaster!")
