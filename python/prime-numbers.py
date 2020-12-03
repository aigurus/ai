def isDiv(num,lst):
    s = 0
    for n in range(2,lst):
        if (num % n == 0):
            s += 1
    if(s>0):
        return True
    else:
        return False

def isPrime(num):
    sqrt = int(num/2)
    if(num % 2 == 0):
        return False
    elif(isDiv(num,sqrt) == True):
        return False
    else:
        return True
        
#
# put your code here
#

for i in range(1, 100):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()