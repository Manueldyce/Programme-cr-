#Trie Croissant et suppression de doublons
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
#suppression du doublons        
for u in range(len(t)-1,-1,-1):
    if t[u]==t[u-1]:
        t.remove(t[u])            
print(t)
