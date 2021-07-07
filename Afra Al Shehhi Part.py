beachQ = ["Which of the beaches in Abu Dhabi do you want to go to? "]
beachP = ["Ladies beach", "Family beach", "Beach for sea activities"]
answer=[beachP]
for index in range(len(beachQ)):
    Q = beachQ[index]
    print (Q)
    Options = beachP[index]
    print ("Option 1:", beachP[0])
    print ("Option 2:", beachP[1])
    print ("Option 3:", beachP[2])
    answers = int(input ("Choose from the following options [1, 2 or 3]: "))
    if answers == 1:
        print ("Al Bateen Ladies Beach, the best beach for women in the UAE")
    elif answers == 2:
        print ("Al Hudayriat Beach, the best place for families")
    elif answers == 3:
        print ("Yas Beach, the best place to freely practice sea activities")
    else:
        print("Sorry it seems you didn't choose one of the options." 
                    "\nInCheck our website for more options.")
