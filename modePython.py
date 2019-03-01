'''
This program was created as a part of the COP 1000 class I was taking.
Simply put, it takes numbers the user inputs, and calculates the mode of them.

Created By: Austin Garrett
'''


#set an list for us to put numbers in
servList = []
modeList = [0,0,0,0,0,0,0,0,0,0,0]

#define function to obtain numbers from a user

def GetInput():
    enternumber = 'y'
    numlist = []
    while enternumber == "y":
        num = int(input("Enter a number:"))
        numlist.append(num)
        enternumber = input("Would you like to enter another number? [y/n]")
    return numlist

#Call the GetInput function

servList = GetInput()

#Tally stuff up

for num in servList:
    modeList[num] += 1

#define function to find mode

def GetMode(modeList):
    i = 1
    mode = 0
    while i < len(modeList):
        if modeList[mode] < modeList[i]:
            mode = i
        i += 1
    return mode

#print mode

print(GetMode(modeList))
