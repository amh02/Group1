# Intro
print("Hey! My name is Reem and I will be your online assistance today.")
name = input("What is your name? ")
gender = input("Enter your gender [F/M]: ").upper()
def greetUser(name, gender):
    if gender == "F":
        print("Welcome Ms."+name.capitalize()+" to the best trip planning in Abu Dhabi!")
    elif gender == "M":
        print("Welcome Mr." + name.capitalize() + " to the best trip planning in Abu Dhabi!")
    else:
        print("Welcome User to the best trip planning in Abu Dhabi!")
greetUser(name, gender)

ask = input(name.capitalize()+" Are you living in Abu Dhabi [Y/N]? ").upper()
if ask == "Y":
    print("We're glad to be part of your journey.\n")
else:
    print("Welcome to the Best Trip Planning Company in Abu Dhabi! We're glad to be part of your journey.\n")

# type  of trip plans
introQ = ["What type looking of trip plan in Abu Dhabi you are looking for? "]
introP = ["For a family trip", "A honeymoon trip", "Trip with a friends"]
answers = [introP]
date = ()
for index in range(len(introQ)):
    Q = introQ[index]
    print(Q)
    Options = introP[index]
    print("Option 1:", introP[0])
    print("Option 2:", introP[1])
    print("Option 3:", introP[2])
    answers = int(input("Choose from the following options [1, 2 or 3]: "))
    if answers == 1:
        date = input("We wish you all the best in your vacation! Is your trip date fixed  (Y/N)? ").upper()
        if date == "Y":
            date = input("Please mention your trip date. eg: 01 Aug ")
            print("Sounds Good! Can't wait to hear your feedback!")
        else:
            print("\nThe best time to visit Abu Dhabi is between April and May or from September to October."
                  "\nCheck your calender and plan your tip to Abu Dhabi.")
            break
    elif answers == 2:
        date = input("Wishing you the best! Is your trip date fixed (Y/N)? ").upper()
        if date == "Y":
            date = input("Please mention your trip date. eg: 01 Aug ")
            print("Sounds Good! Can't wait to hear your feedback!")
        else:
            print("\nThe best time to visit Abu Dhabi is between April and May or from September to October."
                  "\nCheck your calender and plan your tip to Abu Dhabi.")
            break
    elif answers == 3:
        date = input("Enjoy your time together! Is your departure date fixed (Y/N)? ").upper()
        if date == "Y":
            date = input("Please mention your trip date. eg: 01 Aug ")
            print("Sounds Good! Can't wait to hear your feedback!")
        else:
            print("\nThe best time to visit Abu Dhabi is between April and May or from September to October."
                  "\nCheck your calender and plan your tip to Abu Dhabi.")
            break
    else:
        print("\nSorry it seems you didn't choose one of the option."
              "\nYou can email us if you got any question.")
        break

# Days
days = ["\nFor how many days will your trip be?"]
daysAnswer = ["3 days or less", "4 days", "A week", "More than a week"]
for index in range(len(days)):
    D = days[index]
    print(D)
    daysOptions = daysAnswer[index]
    print("Option 1:", daysAnswer[0])
    print("Option 2:", daysAnswer[1])
    print("Option 3:", daysAnswer[2])
    print("Option 3:", daysAnswer[3])
