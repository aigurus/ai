str = input("Enter a String to check for Palindrome: ")
string = ''
for i in str:
    if ord(i) != 32:
        string += i

lowstring = string.lower()

lenstr = len(lowstring)

newstring = ''

for i in range(lenstr-1,-1,-1):
    newstring += lowstring[i]

print(lowstring)
print(newstring)
if lowstring == newstring:
    print("its a palindrome")
else:
    print("Its not a palindrome")