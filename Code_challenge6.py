size = int(input("input the wanted size of your pattern: "))

for j in range(size):
    for k in range(size):
        if j + k == size -1 or j == k:
            print("*", end = " ")
        else: 
            print(" ", end = " ")
    print()