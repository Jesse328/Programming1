print "Hello, World!"
weight = int(input("Enter # of weight to print: "))
length = int(input("Enter # of length to print: "))
width = int(input("Enter # of width to print: "))
height = int(input("Enter # of height to print: "))
cube = length * width * height

if weight > 27 and cube <= 100000:
    print("too heavy")
elif weight <= 27 and cube > 100000:
    print("too large")
elif weight >27 and cube > 100000:
    print("too large and too heavy")
else:
    print("Pass")
   
input()
    
    

    
    
    
    