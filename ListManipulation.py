### Part Three -- your code goes here. 
Numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
Numbers.sort()
ListLen = len(Numbers)
print(ListLen)
Position = 9
while Position >= 0:
    if Numbers[Position] == 1:
        Numbers.pop(Position)
        Position = Position - 1
    else:
        Position = Position - 1
Numbers.append(7)
Numbers.append(8)
print(Numbers)