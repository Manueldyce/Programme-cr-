import random
s= [1,2,3,4,5,6,7,8,9]
while(True):
    if(len(s)==0):
        break
    random.shuffle(s)
    nbr = s[0]
    print(nbr)
    s.remove(nbr)
    rep = input("Continuer..")
   
  
