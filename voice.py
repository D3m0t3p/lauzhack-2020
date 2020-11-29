from gtts import gTTS 
import os
import random as rn
import time

def speak(indi):
    text = indi
    language = 'fr'
    speech = gTTS(text = indi, lang = language, slow = False)
    speech.save("indication.mp3") 
    os.system("start indication.mp3")

origin = (rn.randint(25, 3000)/10, rn.randint(20, 50)/10)
direction = rn.randint(0, 359)
doorList = {1: (13, 0), 2: (23, 0), 3: (33, 0), 4: (43, 0),5: (53, 0),6: (63, 0),7: (73, 0),8: (83, 0),9: (93, 0),10: (103, 0),11: (113, 0),12: (123, 0),13: (133, 0),14: (143, 0),15: (153, 0),16: (163, 0)}
wagon = rn.randint(1, 17)

def giveRightOrientation(direc):
    if(direc > 95 and direc < 265):
        speak("Faire demi-tour")
        direc = (direc - 180) % 360
    elif ((direc < 85 and direc > 0) or (direc > 275 and direc < 360)):
        speak("Tout droit !")
    elif (direc > 85 and direc < 95 ):
        speak("Faire un quart de tour a gauche!")
    elif (direc > 265 and direc < 275):
        speak("Faire un quart de tour a droite!")

def giveDirectionToTrain(og):
    newOg = og
    while (newOg[1] > 1.2) :
        count = 0
        if count >= 3:
            speak("Tout droit !")
        newOg = (newOg[0], newOg[1]  - 0.1)
        print(newOg)
        count = count + 0.1

    speak("S'arrêter !")
    return newOg

def onceAtTrain(og, wag):
    goal = doorList[wag][0]
    if (og[0] < goal - 1):
        speak("Faire un quart de tour vers la gauche pour longer le train !")
        goToDoor(og, goal, True)
    elif (og[0] > goal + 1):
        speak("Faire un quart de tour vers la droite pour longer le train !")
        goToDoor(og, goal, False)
    elif (og[0] < goal + 1 and og[0] > goal - 1):
        speak("Vous êtes devant la porte ! Le bouton est à droite")

def goToDoor(og, goal, goesLeft):
    if (og[0] < goal + 1 and og[0] > goal - 1) :
        speak("Vous êtes devant la porte ! Le bouton est à droite")
        print("position finale : ", og)
        return
    ct = 0
    if ct >= 3:
        speak("Tout droit !")
        ct = 0
    if(goesLeft):
        newOg = (og[0] + 0.1, og[1])
        print(og)
    else :
        newOg = (og[0] - 0.1, og[1])
        print(og)
    ct = ct + 0.1
    time.sleep(0.1)
    goToDoor(newOg, goal, goesLeft)

def main():
    print("wagon :", wagon)
    print("origine :", origin)
    print("direction :", direction)
    giveRightOrientation(direction)
    time.sleep(1)
    midOg = giveDirectionToTrain(origin)

    print("midOg in main: ", midOg)
    onceAtTrain(midOg, wagon)

if __name__ == "__main__":
    main()



#todo: avoir un serveur qui envoit la liste des portes, avec leur coordonnees en meme temps (map?)
#le client (ici) reçoit la liste et a une position originale 
#le client a les fields suivant:
#       - direction originale x
#       - position (x, y) originale x
#       - liste des coordonnees de portes qu'il va recevoir

#protocole:
# recevoir la liste de porte et leurs coordonnees
# calculer la porte la plus proche, update toutes les minutes par ex
# en fonction de la direction de la personne, la mettre face au train
# emmener la personne vers la bande blanche du train
# faire tourner a droite ou a gauche et longer le train
#