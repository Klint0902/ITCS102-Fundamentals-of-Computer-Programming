import getpass

username = "clinton"
password = "la la lost you"

k = input("Input USERNAME ---> ")
l = getpass.getpass("Input PASSWORD ---> ")

if k == username or l == password:
        print("username and password is correct")

else:
        print("lahat ng tao ay nagkakamali")
