def mysplit(strng):
    list = []
    str=""
    strlast=""
    for l in strng:
        
        if(l != " "):
            str += l
  
        if(str != "" and l==" "):
            list.append(str)
            str=""
    findspace = strng.rfind(" ")
    if(findspace != -1):
        for k in range(findspace,len(strng)):
            if(strng[k] != " "):
                strlast += strng[k] 
        if(strlast !=""):
            list.append(strlast)
    return list

#
# put your code here
#

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))