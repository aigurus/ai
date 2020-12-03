inpstr = input("Enter the string to be encrypted: ")
shift = 0
try:
    shift = int(input("Enter number of code shifts required: "))
    if shift<1 or shift>25:
        raise ValueError(shift)
except ValueError:
    print(shift, "is out of allowed range")
else:
    encodedstr=""
    
    for l in inpstr:
        if l.isalpha():
            codel = ord(l)
            newcode = codel+shift
            if codel>=65 and codel<=90:
                if newcode>=65 and newcode<=91:
                    encodedstr += chr(newcode)
                else:
                    circcodel = newcode - 26
                    encodedstr += chr(circcodel)
            elif(codel>=97 and codel <=122):
                if newcode>=97 and newcode<=122:
                    encodedstr += chr(newcode)
                else:
                    circcodes = newcode - 26
                    encodedstr += chr(circcodes)
        else:
            encodedstr += l
                
    print("the encoded string is :", encodedstr)
            
             