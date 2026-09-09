#if and elif condition

#make a python program that identifies age group 

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 1 and age <= 2:
    print("The age is considered as toddler")

elif age >= 3 and age <= 5:
    print("The age is consiered as preschool/middle Childhood")

elif age >= 6 and age <= 12:
    print("The age is considered as Middle Childhood") 
    
elif age >= 13 and age <= 19:
    print("The age is considered as Teenager")
    
elif age >= 20 and age <= 39:
    print("The stage is considered as Early Adulthood")
    
elif age >= 40 and age <= 59:
    print("The satge is considered as Midlle Adulthood")
    
elif age >= 60:
    print("The age is considered as Seniority/Older Adulthood")
    


    
  
