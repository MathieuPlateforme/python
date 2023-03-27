#def Add(number1, number2):
#    return number1 + number2
#
#print(Add(1, 2))
#
#def Prenom():
#    return input("Quel est votre prénom ? ")
#
#print("Hello " + Prenom())
#
#def Nombre():
#    numberArray = []
#    for i in range(0, 5):
#        number = input("Entrez un nombre : ")
#        numberArray.append(int(number))
#        numberArray.sort()
#    return numberArray
#
#for value in Nombre():
#    print(value)
#
#def NombreEntier():
#    for i in range(1, 101):
#        if i % 3 == 0 and i % 5 == 0:
#            print("FizzBuzz")
#        elif i % 3 == 0:
#            print("Fizz")
#        elif i % 5 == 0:
#            print("Buzz")
#
#NombreEntier()

#def printRectangle():
#    width = int(input("Entrez la largeur du rectangle : "))
#    height = int(input("Entrez la hauteur du rectangle : "))
#    printHeight = "|"
#    printWidth = "-"
#    printBlank = " "
#    for i in range(0, height):
#        if (i == 0 or i == height - 1):
#            print(printHeight + (printWidth * width) + printHeight)
#        else:
#            print(printHeight + (printBlank * width) + printHeight)
#
#printRectangle()
#
#def printTriangle():
#    height = int(input("Entrez la hauteur du triangle : "))
#    printHeightLeft = "/"
#    printHeightRight = "\\"
#    printWidth = "_"
#    printBlank = " "
#    for i in range(0, height):
#        if (i == height - 1):
#            print(printHeightLeft + (printWidth*(height*2-2)) +printHeightRight)
#        else:
#            print(printBlank * (height - i - 1) + printHeightLeft + (printBlank * (i*2)) + printHeightRight)
#
#printTriangle()

#def roundedNumbers():
#    numberList = [1, 3, 6, 8, 12, 15, 18, 22, 25, 28, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
#    for i in range(0, len(numberList)):
#        if (numberList[i] % 5 > 2):
#            print(str(numberList[i]) + " rounded is " + str(numberList[i] + (5 - (numberList[i] % 5))))
#    return numberList
#
#roundedNumbers()

# make a regex lowercase and letter only
#def truc():
#    import re
#    regex = re.compile(r'[^a-z]')
#    string = input("Entrez un mot : ")
#    if (regex.search(string) == None):
#        print(string)
#    elif (string == "Q"):
#        print("Bye !")
#    else:
#        print("Erreur, veuillez entrer un mot sans caractères spéciaux ou majuscules (Entrée 'Q' pour quitter)")
#        truc()

#truc()