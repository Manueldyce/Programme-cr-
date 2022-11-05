print("---------------[CALCULATRICE]----------------")
print("-         (+)__________-> ADDITION          ")
print("-         (-)__________-> SOUSTRACTION      ")
print("-         (*)__________-> MULTIPLICATION    ")
print("-         (/)__________-> DIVISION          ")
while(True):
    a=int(input("Veuillez saisir le 1er nombre: "))
    b=int(input("Veuillez saisir le  second nombre: "))
    s=input("Veuillez saisir  le symbole de l'opération celon le menu: ")
    if s=="+":
        res=a+b
        print("Le resultat de",a,"+",b,"est: ",res)
    elif s=="-":
        res=a-b
        print("Le resultat de",a,"-",b,"est: ",res)
    elif s=="*":
        res=a*b
        print("Le resultat de",a,"*",b,"est: ",res)
    elif s=="/":
        if b==0:
            print("ERREUR, Entrer un diviseur différent de 0")
        else:
            res=a/b
            print("Le resultat de",a,"/",b,"est: ",res)
    else:
        print("entrez un symbole valide")
        
