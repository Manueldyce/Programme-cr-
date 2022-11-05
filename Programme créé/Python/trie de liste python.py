#Selection par trie du maximum
t=[]
#Remplissage du tableau
for j in range(1,7):
    nbr=int(input("entrer les 6 différents nombre: "))
    t.append(nbr)
#Rangement du tableau
for i in range(len(t)):
    for j in range(len(t)):
        if t[i]<=t[j]:
            t[i],t[j]=t[j],t[i]

#Affichage du tableau trié
for u in range(0,6):
    print(t[u])
