#Code du jeu
import random , pyttsx3
#System Aléatoire de l'IA
print("~~JEU PIERRE-PAPIER-CISEAU~~")
res= ["Pierre","Papier","Ciseau"]
while(True):
    random.shuffle(res)
    random.shuffle(res)
    random.shuffle(res)
    nbr = res[0]
    choix= str( input("°Pierre\n°Papier\n°Ciseau\nVeuillez saisir votre choix: "))
    print("moi je joue: ",nbr)
    if (nbr=="Pierre" and choix =="Ciseau") or (nbr =="Papier" and choix =="Pierre") or (nbr =="Ciseau" and choix =="Papier"):
        engine = pyttsx3.init()
        text3="je reste la meilleure "
        engine.say(text3)
        engine.runAndWait()
        print("VOUS AVEZ PERDU")
        print("continuous...")    
    elif (choix =="Pierre" and nbr =="Ciseau") or (choix =="Papier" and nbr =="Pierre") or (choix =="Ciseau" and nbr =="Papier"):
        engine = pyttsx3.init()
        text2="Bon match, Vous m'avez surpassé félicitation a-vous "
        engine.say(text2)
        engine.runAndWait()
        print("BIEN JOUEE")
        print("continuous...")   
    elif nbr == choix :
        engine = pyttsx3.init()
        text1="Match nul "
        engine.say(text1)
        engine.runAndWait()
        print("EGALITE")
        print("continuous...")
