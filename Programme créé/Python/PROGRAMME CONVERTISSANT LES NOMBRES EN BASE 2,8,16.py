t=[]
nbr=int(input("Veuillez entrer un nombre a convertir: "))
x=nbr
print("entrer 1-->base2;  2-->base8;  3-->base16")
choix=int(input("Vers quelles base souhaiter vous convertir:"))
if choix==1:
    while(nbr>=2):
        res=nbr%2
        t.append(res)
        nbr=nbr//2
        if(nbr<2):
            t.append(nbr)
            break
    reverse=t[::-1]
    v=len(reverse)
    print(x,"en base 2 sur",v,"bits est:",reverse)
if choix==2:
    while(nbr>=8):
        res=nbr%8
        t.append(res)
        nbr=nbr//8
        if(nbr<8):
            t.append(nbr)
            break
    reverse=t[::-1]
    v=len(reverse)
    print(x,"en base 8 sur",v,"bits est:",reverse)
if choix==3:
    while(nbr>=16):
        res=nbr%16
        t.append(res)
        nbr=nbr//16
        if(nbr<16):
            t.append(nbr)
            break
    reverse=t[::-1]
    v=len(reverse)
    print(x,"en base 16 sur",v,"bits est:",reverse)
if choix==3:
    while(nbr>=16):
        res=nbr%16
        t.append(res)
        nbr=nbr//16
        if(nbr<16):
            t.append(nbr)
            break
    reverse=t[::-1]
    for index, value in enumerate(reverse):
        if value == 10:
          reverse[index] ='A'
        if value == 11:
          reverse[index] = 'B'
        if value == 12:
          reverse[index] = 'C'
        if value == 13:
          reverse[index] = 'D'
        if value == 14:
          reverse[index] = 'E'
        if value == 15:
          reverse[index] = 'F' 
    v=len(reverse)
    print(x,"en base 16 sur",v,"bits est:",reverse)
