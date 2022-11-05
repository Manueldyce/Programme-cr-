#Programme permettant de vérifier la sûreté d'un pont avec une fonction
d=str(input("Entrer le code du pont: "))
def Mean(d):
    z='1'
    for i in  d:
         if i!='#' :
                z='0'
                x="Cet pont n'est pas sûre"
                return(x)
                break
    if z!= '0':
        x="Cet pont est sûre"
        return(x)
print(Mean(d))
