#Programme permettant de vérifier la sûreté d'un pont avec une fonction
d=str(input("Entrer une phrase ou un mot (NB:tout en miniscule svp): "))
def Mean(d):
    choix=str(input("Entrer la lettre: "))
    x=0
    for i in range(len(d)):
        if choix==d[i]:
            x=x+1
    if x==0:
        u="La lettre entrée n'est pas dans la phrase"
        
    else:u=(x*100)/len(d)
    return u
print(Mean(d),"%")
