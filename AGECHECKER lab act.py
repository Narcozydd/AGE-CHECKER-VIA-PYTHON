#function
def agechecker():
    age = int(input("Enter your age:\n > "))
    if age < 0: 
        print("you entered an invalid age")
    elif age <= 12:
        print("you are a CHILD.")
    elif age <= 19:
        print("you are a TEEN.")
    elif age <= 64:
        print("you are a ADULT.")
    else:
        print("you are a SENIOR.")

#MAIN
agechecker()

while True:
    a = input("do you want to run the program again?(yes/no):").strip().lower()
    if a == "yes":
        print("Undestood, running program again \n >")
        agechecker()
    else:
        print("Exiting Program")
        break
    
