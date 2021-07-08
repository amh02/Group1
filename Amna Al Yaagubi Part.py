touristicQ = ["which of the places in Abu Dhabi do you want to visit?"]
touristicp = ["Zayed Mosque", "Yas Island", "Louver Museum"]
answer=[touristicp]
for index in range(len(touristicQ)):
    Q = touristicQ[index]
    print (Q)
    options = touristicp[index]
    print ("option 1:", touristicp[0])
    print ("option 2:", touristicp[1])
    print ("option 3:", touristicp[2])
    answers = int(input("Choose from the following options [1, 2 or 3]:"))
    if answers == 1:
        print ("Zayed Mosque, the biggest mosque in Abu Dhabi")
    elif answers == 2:
        print ("Yas Island, the most beautiful entertainment area!!")
    elif answers == 3:
        print ("Louver Museum, A beacon that brings together the intellctual and artistic creations of different civilization")
    else:
        print ("sorry, it seems you did not choose one of the options")
