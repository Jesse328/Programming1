print "Hello, World!"
dozen = int(input("Enter # of dozen to print"))
price = 0.0
bill = 0.0

if dozen > 0 and dozen <= 4:
    print("price = 0.50")
elif dozen > 4 and dozen <= 6:
    print("price = 0.45")
elif dozen > 6 and dozen <= 11:
    print("price = 0.40")
elif dozen > 11:
    print("price = 0.35")
    
else:
    print("Invalid # of dozen")
 
bill = price * dozen
input()