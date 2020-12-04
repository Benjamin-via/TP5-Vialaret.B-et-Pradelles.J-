#feature 1 à 3
def hello(nom):

    if nom is None:
        return 'Hello, my friend'
    carac = list(nom)

    if len(carac) == 0 or carac[0] == ' ':
        return 'Hello, my friend'

    nom = premiereEnMaj(nom, carac)
    if nomMaj(carac) == 1:
        affichage = 'HELLO ' + nom +'!'
        return affichage

    affichage = 'Hello ' + nom
    return affichage

#feature 4 à 6
def hello2(nom):

    affichage = ''
    tableauNom = plusieurNom(nom)
    nomEnMaj = []
    nomEnMin = []
    if len(tableauNom)>=1:
        for i in tableauNom:
            carac = list(i)
            if(nomMaj(carac)==1):
                nomEnMaj.append(i)
            else:
                nomEnMin.append(i)
        if nomEnMin != []:
            affichage = 'Hello'
            for i in range (0, len(nomEnMin)):
                affichage = affichage+ ', ' + str(nomEnMin[i])
            affichage = affichage + '.'
        if nomEnMaj == []:
            return affichage
        else:
            affichage = affichage + ' AND HELLO'
            for i in range (0, len(nomEnMaj)):
                affichage = affichage + ', ' + str(nomEnMaj[i])
            affichage = affichage + ' !'
        return affichage
    return None

#feature 7 à 12
def hello3(nom):
    tableauNom = ignore(plusieurNom(nom))
    for i in range (0,len(tableauNom)):
        carac = list(tableauNom[i])
        tableauNom[i] = premiereEnMaj(tableauNom[i], carac)
    tableauCompter = compt(tableauNom)
    if helloWorld(tableauCompter) == 0:
        affichage = 'Hello'
        return affichage + affichageStandar(tableauCompter)
    else:
        return helloWorld(tableauCompter)

#feature 13 à 14
def yoda(nom):
    tableauNom = ignore(plusieurNom(nom))
    for i in range(0, len(tableauNom)):
        carac = list(tableauNom[i])
        tableauNom[i] = premiereEnMaj(tableauNom[i], carac)
    tableauCompter = compt(tableauNom)
    yoda = 0
    for i in range (0,len(tableauCompter)):
        if tableauCompter[i][0].lower() == 'yoda':
            yoda = 1
    if yoda == 0:
        if helloWorld(tableauCompter) == 0:
            affichage = 'Hello'
            return affichage + affichageStandar(tableauCompter)
        else:
            return helloWorld(tableauCompter)
    else:
        if helloWorld(tableauCompter) == 0:
            affichage = ', Hello.'
            affichage2 = affichageStandar(tableauCompter)
            carac = list(affichage2)
            del carac[0]
            del carac[0]
            del carac[-1]
            affichage2 = "".join(carac)
            return affichage2 + affichage
        else:
            return 'World, Hello'


#feature 15 à 16
def hello4(nom):
    tableauNom = ignore(plusieurNom(nom))
    for i in range(0, len(tableauNom)):
        carac = list(tableauNom[i])
        tableauNom[i] = premiereEnMaj(tableauNom[i], carac)
    tableauCompter = compt(tableauNom)
    return affichageStandarGuest(tableauCompter)

#feature 17
def hello17(nom):
    tableauNom = plusieurNom17(nom)
    for i in range(0, len(tableauNom)):
        carac = list(tableauNom[i])
        tableauNom[i] = premiereEnMaj(tableauNom[i], carac)
    tableauCompter = compt(tableauNom)
    if helloWorld(tableauCompter) == 0:
        affichage = 'Hello'
        return affichage + affichageStandar(tableauCompter)
    else:
        return helloWorld(tableauCompter)


def affichageStandar(tableauCompter):
    affichage =''
    for i in range(0, len(tableauCompter) - 1):
        if tableauCompter[i][1] == 1:
            affichage = affichage + ', ' + tableauCompter[i][0]
        else:
            affichage = affichage + ', ' + tableauCompter[i][0] + ' (x' + str(tableauCompter[i][1]) + ')'
    if tableauCompter[len(tableauCompter) - 1][1] == 1:
        affichage = affichage + ' and ' + tableauCompter[len(tableauCompter) - 1][0] + '.'
    else:
        affichage = affichage + ' and ' + tableauCompter[len(tableauCompter) - 1][0] + ' (x' + str(
            tableauCompter[len(tableauCompter) - 1][1]) + ').'
    return affichage


def affichageStandarGuest(tableauCompter):
    affichage ='Hello'
    lastGuest = 0
    for i in range(0, len(tableauCompter) - 1):
        carac = list(tableauCompter[i][0])
        if carac[0] == '*' and carac[-1] == '*':
            if lastGuest == 0:
                lastGuest = 1
                del carac[0]
                del carac[-1]
                nom2 = "".join(carac)
                affichage = affichage + ', our special guest ' + nom2 + ','
            else:
                lastGuest = 1
                del carac[0]
                del carac[-1]
                nom2 = "".join(carac)
                affichage = affichage + ' & ' + nom2 + ','
        else:
            lastGuest = 0
            affichage = affichage + ', ' + tableauCompter[i][0]
    carac = list(tableauCompter[-1][0])
    if carac[0] == '*' and carac[-1] == '*':
        if lastGuest == 0:
            del carac[0]
            del carac[-1]
            tableauCompter[i][0] = "".join(carac)
            affichage = affichage + ', our special guest ' + tableauCompter[i][0]
        else:
            del carac[0]
            del carac[-1]
            nom2 = "".join(carac)
            affichage = affichage + ' & ' + nom2 + '.'
    else:
        affichage = affichage + ' and ' + tableauCompter[len(tableauCompter) - 1][0] + '.'
    return affichage


def helloWorld(tableauCompter):
    tousEnMaj = 1
    for i in tableauCompter:
        if nomMaj(i[0]) == 0:
            tousEnMaj = 0
    if tousEnMaj == 1 and len(tableauCompter) > 5:
        return  'HELLO, WORLD !'
    elif len(tableauCompter) > 5:
        return 'Hello, world !'
    else:
        return 0


def nomMaj(carac):
    nomEnMaj = 1
    for i in carac:
        if ord(i) >= 97:
            nomEnMaj = 0
    return nomEnMaj


def plusieurNom(nom):

    tableauNom = nom.replace(' ','').split(',')
    return tableauNom


def plusieurNom17(nom):
    tableauNom = nom.replace(' ','').split('"')
    return tableauNom


def ignore(tableauNom):
    for i in tableauNom:
        carac = list(i)
        if carac[0] == "!":
            nomASuppr = i.replace('!','')
            tableauNom.remove(nomASuppr)
            tableauNom.remove('!'+nomASuppr)
    return tableauNom


def premiereEnMaj(nom, carac):
    if ord(carac[0]) >= 97:
        codeascii = ord(carac[0]) - 32
        carac[0] = chr(codeascii)
        nom = "".join(carac)
    return nom


def compt(tableauNom):
    listeTuple = []
    for i in tableauNom:
        exist = 0
        for j in listeTuple:
            if i == j[0]:
                exist = 1
        if exist == 0:
            listeTuple.append((i,tableauNom.count(i)))
    return listeTuple