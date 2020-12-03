string1 = input("Enter a text as base: ")
string2 = input("Enter a text to compare: ")

string1 = string1.replace(" ","")
string2 = string2.replace(" ","")
string3 = ""
string4 = ""
print(string1)
print(string2)
if string1 == string2:
    print("Both the strings should be different.")
elif len(string1)==0 or len(string2)==0:
    print("Eneter some characters. Dont just enter space.")
elif len(string1) != len(string2):
    print("use all the original characters atleast once.")
else:
    #string3 = sorted(list(string1.lower()))
    #string4 = sorted(list(string2.lower()))
    
    string3 = sorted(string1.lower())
    string4 = sorted(string2.lower())
    
print(string3)
print(string4)
if string3 == string4:
    print("Anagrams")
else:
    print("Not Anagrams")