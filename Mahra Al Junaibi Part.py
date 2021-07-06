restQ = ["What type of restaurant you are looking for? "]
restP = ["Italian restaurant", "Indian restaurant", "International restaurant"]
answer=[restP]
for index in range(len(restQ)):
    Q = restQ[index]
    print(Q)
    Options = restP[index]
    print("Option 1:", restP[0])
    print("Option 2:", restP[1])
    print("Option 3:", restP[2])
    answers = int(input("Choose from the following options [1, 2 or 3]: "))
    if answers == 1:
        print("Prego’s restaurant good choice for you")
    elif answers == 2:
        print("Asha’s restaurant is great choice for you")
    elif answers == 3:
        print("The cheesecake factory best choice")
    else:
        print("Sorry it seems you didn't choose one of the option."
              "\nCheck our website for more options.")
