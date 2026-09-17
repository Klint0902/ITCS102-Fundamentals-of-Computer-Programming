age = int(input("Enter your age: "))
is_employed = input("Are you employed? (yes/no): ")
credit_score = eval(input("Enter your credit score: "))
annual_income = eval(input("Enter your annual income: "))
has_collateral = input("Do you have collateral? (yes/no): ")

#Tier 1
if age >= 21 and is_employed == "yes":
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



   

