#Programme vérifiant si un nbr entier est premier
a=1
while(a==1):    
   nbr= int(input("Veuiller entrer le nombre a verifier: "))
   #Traitement
   z=0
   for i in range(2,nbr):
      if (nbr%i==0):
         z=1
         break
   if (z==1):
      print(nbr,"n'est pas premier") 
   else:
      print(nbr,"est un nombre premier")