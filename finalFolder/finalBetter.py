
def letterConvert(listy, indexx): #replaces all column letters with number
    letters = ['a','b','c','d','e','f','g']
    for k in range(len(listy)):    
        for x in range(len(letters)): # for all in list
            if letters[x] == listy[k][indexx]:
                listy[k][indexx] = x + 1
    return listy


def checkHorizontal(listy): #listy is all player checkers
    listy = letterConvert(listy, 0) #coverting listy to numbers
    for x in listy:
        coolList = []
        for y in listy:
            if (x[1] == y[1]): # if they share the same x coord (if they're in same row)
                coolList.append(y[0])# add t
    print(coolList)
    return checkColumn(coolList)

def checkVertical(listy): #listy is all player checkers
    listy = letterConvert(listy, 0) #coverting listy to numbers
    for x in listy:
        coolList = []
        for y in listy:
            if (x[0] == y[0]): # if they share the same y coord (if they're in same row)
                coolList.append(y[1])# add t
    print(coolList)
    return checkColumn(coolList)

def checkDiagonal(listy): #listy is all player checkers
    listy = letterConvert(listy, 0) #coverting listy to numbers
    counter = 1
    coolList = []
    for x in listy:
        for y in listy:
            xo = x[0]
            yo = y[0]
            xi = x[1]
            yi = y[1] #if coords x and y are x+1 and y+1
            if (((xo == yo + counter) and (xi == yi + counter)) or ((xo == yo - counter) and (xi == yi - counter))):
                counter += 1 #add to counter
    if(counter >= 4):
        return True
    else:
        return False
    
def checkColumn(column):
    counter = 1
    Ncounter = 1
    for c in column:
        for d in column:
            if(c == d + counter):
                counter += 1
            if(c == d - Ncounter):
                Ncounter += 1
        print(str(Ncounter) + str(counter))
        if((counter >= 4) or (Ncounter >= 4) or (counter + Ncounter >= 4)):
            return True
        else:
            return False
                
player1 = [['a',1],['b',1],['c',1],['d',1]]
player2 = [['a',1],['a',2],['a',3],['a',4]]
player3 = [['a',1],['b',2],['c',3],['d',4]]
player4 = [['b',3],['c',4],['d',5],['e',6]]
