n=int(input("Veuillez entrer un nombre pour l'operation: "))
s=True
a=0
x=n
while(s==True):
    for i in range(1,n+1):
        if (n%i)==0 :
            a=a+i
    if n>1:n=n-1
    else:s=False        
print("La somme des diviseurs du factorielle de",x," est: " ,a) 
   

