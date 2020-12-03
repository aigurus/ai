FirstRow ={"1":"  #","2":"###","3":"###","4":"# #","5":"###","6":"###","7":"###"
           ,"8":"###","9":"###","0":"###"}

SecondRow ={"1":"  #","2":"  #","3":"  #","4":"# #","5":"#  ","6":"#  ","7":"  #"
           ,"8":"# #","9":"# #","0":"# #"}

ThirdRow ={"1":"  #","2":"###","3":"###","4":"###","5":"###","6":"###","7":"  #"
           ,"8":"###","9":"###","0":"# #"}

FourthRow ={"1":"  #","2":"#  ","3":"  #","4":"  #","5":"  #","6":"# #","7":"  #"
           ,"8":"# #","9":"  #","0":"# #"}

FifthRow ={"1":"  #","2":"###","3":"###","4":"  #","5":"###","6":"###","7":"  #"
           ,"8":"###","9":"###","0":"###"}
           
def FirRow(i):
    if(i == "1"):
        print(FirstRow["1"],end=" ");
    if(i == "2"):
        print(FirstRow["2"],end=" ");
    if(i == "3"):
        print(FirstRow["3"],end=" ");
    if(i == "4"):
        print(FirstRow["4"],end=" ");
    if(i == "5"):
        print(FirstRow["5"],end=" ");
    if(i == "6"):
        print(FirstRow["6"],end=" ");
    if(i == "7"):
        print(FirstRow["7"],end=" ");
    if(i == "8"):
        print(FirstRow["8"],end=" ");
    if(i == "9"):
        print(FirstRow["9"],end=" ");
    if(i == "0"):
        print(FirstRow["0"],end=" ");

def SecRow(i):
    if(i == "1"):
        print(SecondRow["1"],end=" ");
    if(i == "2"):
        print(SecondRow["2"],end=" ");
    if(i == "3"):
        print(SecondRow["3"],end=" ");
    if(i == "4"):
        print(SecondRow["4"],end=" ");
    if(i == "5"):
        print(SecondRow["5"],end=" ");
    if(i == "6"):
        print(SecondRow["6"],end=" ");
    if(i == "7"):
        print(SecondRow["7"],end=" ");
    if(i == "8"):
        print(SecondRow["8"],end=" ");
    if(i == "9"):
        print(SecondRow["9"],end=" ");
    if(i == "0"):
        print(SecondRow["0"],end=" ");
 
 
def ThiRow(i):
    if(i == "1"):
        print(ThirdRow["1"],end=" ");
    if(i == "2"):
        print(ThirdRow["2"],end=" ");
    if(i == "3"):
        print(ThirdRow["3"],end=" ");
    if(i == "4"):
        print(ThirdRow["4"],end=" ");
    if(i == "5"):
        print(ThirdRow["5"],end=" ");
    if(i == "6"):
        print(ThirdRow["6"],end=" ");
    if(i == "7"):
        print(ThirdRow["7"],end=" ");
    if(i == "8"):
        print(ThirdRow["8"],end=" ");
    if(i == "9"):
        print(ThirdRow["9"],end=" ");
    if(i == "0"):
        print(ThirdRow["0"],end=" ");
        
def FouRow(i):
    if(i == "1"):
        print(FourthRow["1"],end=" ");
    if(i == "2"):
        print(FourthRow["2"],end=" ");
    if(i == "3"):
        print(FourthRow["3"],end=" ");
    if(i == "4"):
        print(FourthRow["4"],end=" ");
    if(i == "5"):
        print(FourthRow["5"],end=" ");
    if(i == "6"):
        print(FourthRow["6"],end=" ");
    if(i == "7"):
        print(FourthRow["7"],end=" ");
    if(i == "8"):
        print(FourthRow["8"],end=" ");
    if(i == "9"):
        print(FourthRow["9"],end=" ");
    if(i == "0"):
        print(FourthRow["0"],end=" ");
        
def FifRow(i):
    if(i == "1"):
        print(FifthRow["1"],end=" ");
    if(i == "2"):
        print(FifthRow["2"],end=" ");
    if(i == "3"):
        print(FifthRow["3"],end=" ");
    if(i == "4"):
        print(FifthRow["4"],end=" ");
    if(i == "5"):
        print(FifthRow["5"],end=" ");
    if(i == "6"):
        print(FifthRow["6"],end=" ");
    if(i == "7"):
        print(FifthRow["7"],end=" ");
    if(i == "8"):
        print(FifthRow["8"],end=" ");
    if(i == "9"):
        print(FifthRow["9"],end=" ");
    if(i == "0"):
        print(FifthRow["0"],end=" ");
userinput = int(input("Enter a number to print: "))
for i in str(userinput):
    FirRow(i)
print(end="\n")
for i in str(userinput):
    SecRow(i) 
print(end="\n")
for i in str(userinput):
    ThiRow(i)
print(end="\n")
for i in str(userinput):
    FouRow(i)
print(end="\n")
for i in str(userinput):
    FifRow(i)
    

