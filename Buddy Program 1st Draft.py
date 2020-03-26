import random

databaseOFpeople = open("KylesList.txt","r")
dOFp = databaseOFpeople.read()
databaseOFpeople.close()

eachperson = dOFp.split(',')

def matchmaker(coworkers):
    bud = []
    maxi = len(coworkers)-1
    maxim = maxi-1
    i = 0
    while i < maxi:
        feature = coworkers[i].split()
        bud.append(feature)
        i = i+1

    #print (random.randint(1,maxi))
    alreadytaken = []

    for buddy in bud:
        #print(buddy)
        kicker = 1
        while kicker == 1:
            newNumber = random.randint(0,maxim)
            newHire = (bud[newNumber])
            if buddy[0] == newHire[0]:
                kicker = 1
            elif buddy[2] == newHire[2]:
                kicker = 1
            elif buddy[3] == newHire[3]:
                kicker = 1
            elif buddy[4] == newHire[4]:
                kicker = 1
            else:
                alreadytaken.append(newNumber)
                kicker = 0
        print(buddy[1], " is with ", newHire[1])
    print("Already Taken")
    print(alreadytaken)
    return

matchmaker(eachperson)
