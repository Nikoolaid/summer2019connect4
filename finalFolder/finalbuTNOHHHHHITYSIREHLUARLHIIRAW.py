

def findIndexThing(listy, thing): #returns index of selected item if in list
    for x in range(len(listy)):
        if(thing == listy[x]):
            return x
        elif(x == len(listy)):
            return -1


        #example list: [a1, a2, a3, a4] wins vertical
        #[a1, b1, c1, d1] wins horizontal
        #[a1,b2,c3,d4] wins diagonal or [a4,b3,c2,d1]


def letterConvert(listy, indexx): #replaces all column letters with number
    letters = ['a','b','c','d','e','f','g']
    for k in range(len(listy)):    
        for x in range(len(letters)): # for all in list
            if letters[x] == listy[k][indexx]:
                listy[k][indexx] = x + 1
    return listy

'''
def checkHorizontal(listy): #checks if there is a win condition in horizontal
    counter = 1 # count
    Ncounter = 1
    coolList = []
    listy = letterConvert(listy, 1) #convert list into number list
    for j in range(len(listy)):
        for k in range(len(listy)):
            if((listy[j][0]) == (listy[k][0])):
                coolList.append(listy[j])
        for s in range(len(coolList)):
            if (coolList[s][1]) == (listy[j][1] + counter):
                counter += 1
            elif ((coolList[s][1]) == (listy[j][1] - Ncounter)):
                Ncounter += 1
    if((counter >= 4) or (Ncounter >= 4) or (counter + Ncounter >= 4)):
        return True
    else:
        return False
'''
#def checkHorizontal(listy):
   # for r in listy:


def checkHorizontal2(listy):
    for x in listy:
        coolList = []    
        for y in listy:
            if (x[0] == y[0]):
                coolList.append(y[0])
            checkColumn(coolList)

def checkColumn(column):
    counter = 1
    Ncounter = 1
    for c in column:
        for d in column:
            if(c == d + counter):
                counter += 1
            if(c == d - Ncounter):
                Ncounter += 1
    if((counter >= 4) or (Ncounter >= 4) or (counter + Ncounter >= 4)):
        return True
    else:
        return False        

