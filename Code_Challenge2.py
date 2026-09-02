print("================= BANK DENOMINATION ================")

Amount = eval(input("Amount of money to deposit ? ------> "))
print()

print("Money to deposit ----->", Amount)

print("thousands =", Amount // 1000) 

friv = Amount // 1000 * 1000

print("five hundred/s =",  (Amount - friv) // 500)

tuhan = (Amount - friv) % 500 

print("two hundred/s =", tuhan // 200)

wanhan = tuhan % 200

print("one hundred/s =", wanhan // 100)

pepti = wanhan % 100

print("fifty/fifties =", pepti // 50) 

venti = pepti % 50 

print("twenty/twenties =", venti // 20)

thins = venti % 20

print("ten/s =", thins // 10)

fight = thins % 10

print("five/s =", fight // 5)

juans = fight % 5 

print("one/s =", juans // 1)




