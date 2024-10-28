### Part Four -- your code goes here. 
import random
NumList = [0,0,0,0,0,0,0,0,0,0]
for x in range(0, 9):
    NumList[x] = random.randint(1 , 100)
position = 0
ListLen = int(len(NumList))
while position < ListLen:
    if NumList[position] % 2 == 0:
        NumList.pop(position)
    else:
        position = position + 1
    ListLen = int(len(NumList))
#couldnt get it working with a for loop sorry
print(NumList)