c0 = int(input("Enter a natural number"))

while(c0 != 1):
    check = c0 % 2
    if check == 0:
        c0 = c0/2
        print(c0)
    else:
        c0 = 3*c0 + 1
        print(c0)
    
    
