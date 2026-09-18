import getpass

print("Creating an account is required")

k = input("\nEnter your email: ")
l = input("Create your username: ")
m = input("Create your password: ")

print("\nAcount created, Please continue to log in page")

username = input("\nEnter your username: ")
password = input("Enter your password: ")

if username == l and password == m:
    print("\nAccount logged in, you can now make a loan")
else:
    print("\nAccount not found")


username = str(input("\nEnter your username: "))
password = str(getpass.getpass("Enter your password: "))

print("Fill the following in order to make a loan")
age = int(input("\nEnter your age: "))
is_employed = input("Are you employed? (yes/no): ")
credit_score = eval(input("Enter your credit score: "))
annual_income = eval(input("Enter your annual income: "))
has_collateral = input("Do you have collateral? (yes/no): ")
collateral_description = input("What kind of collateral will you provide: ")
collateral_value = float(input("what is the value of your given collateral: "))

if collateral_value > 30000:
    print("Collateral value is accepted, you can continue to make a loan")
else:
    print("Collateral value too low, loan request denied")
#Tier 1
if 21 >= age <= 65 and is_employed == "yes":
    if credit_score >= 750:
        if annual_income >= 100000:
            print("Approved with an interest of 4.5%")
        else:
            print("Approved with an interest of 5.0%")
            #Tier 2
    elif 600 <= credit_score < 750:
        if has_collateral == "yes":
            print("Aprroved with an interest of 7.0")
        elif annual_income < 40000:
            print("Approved with an interest of 9.5")
        else:
            print("Approved with an interest of 8.0")
        #tier 3
    else:
        print("Rejected: Credit Score too low")        
else: 
        print("Rejected: Failed baseline criteria")



   