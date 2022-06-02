from PIL import Image
import os
from os import listdir
from random import random

#attribute folders:
backgrounds = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\Backgrounds"
back_wings = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\Back_Wings"
tail = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\Tail"
bodies = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\Bodies"
eyes = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\Eye"
front_wings = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\Front_Wings"
hair = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\Hair"
horn = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\Horn"
helmets = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\Helmet"
sword = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\sword"
accessories = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\accessories"
#final images destination
finalImages = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run\Blessings"

#defining an empty images array which we'll use to come up with each final image
images = []
for i in range(len(os.listdir(r"C:\Users\meren\OneDrive\Masaüstü\Blessings Warrior Run"))-2):
    images.append("")

background_names = {
    "WARRIOR GRADIENT BACKGROUND 1.png":,
    "WARRIOR GRADIENT BACKGROUND 2.png":,
    "WARRIOR GRADIENT BACKGROUND 3.png":,
    "WARRIOR GRADIENT BACKGROUND 4.png":,
    "WARRIOR GRADIENT BACKGROUND 5.png":,
    "WARRIOR GRADIENT BACKGROUND 6.png":,
    "WARRIOR GRADIENT BACKGROUND 7.png":,
    "WARRIOR GRADIENT BACKGROUND 8.png":,
    "WARRIOR GRADIENT BACKGROUND 9.png":,
    "WARRIOR GRADIENT BACKGROUND 10.png":,
    "WARRIOR RARE BACKGROUND 1.png":,
    "WARRIOR RARE BACKGROUND 3.png":,
    "WARRIOR RARE BACKGROUND 4.png":,
    "WARRIOR RARE BACKGROUND 2.png":,
    "WARRIOR RARE BACKGROUND 5.png":
}
bWing_names = {
    "WARRIOR BACK WING 1.png":,
    "WARRIOR BACK WING 2.png":,
    "WARRIOR BACK WING 3.png":,
    "WARRIOR BACK WING 4.png":,
    "WARRIOR BACK WING 5.png":
}
tail_names = {
    "WARRIOR TAIL 1.png":,
    "WARRIOR TAIL 2.png":,
    "WARRIOR TAIL 3.png":,
    "WARRIOR TAIL 4.png":,
    "WARRIOR TAIL 5.png":
}
body_names = {
    "WARRIOR BODY 4.png":,
    "WARRIOR BODY 6.png":,
    "WARRIOR BODY 1.png":,
    "WARRIOR BODY 3.png":,
    "WARRIOR BODY 7.png":,
    "WARRIOR BODY 8.png":
}
eye_names = {
    "WARRIOR EYE F1.png":,
    "WARRIOR EYE F2.png":,
    "WARRIOR EYE F3.png":,
    "WARRIOR EYE F4.png":,
    "WARRIOR EYE M1.png":,
    "WARRIOR EYE M2.png":,
    "WARRIOR EYE M3.png":,
    "WARRIOR EYE M4.png":
}
fWing_names = {
    "WARRIOR FRONT WING 1.png":,
    "WARRIOR FRONT WING 2.png":,
    "WARRIOR FRONT WING 3.png":,
    "WARRIOR FRONT WING 4.png":,
    "WARRIOR FRONT WING 5.png":
}
hair_names = {
    "WARRIOR HAIR 1.png":,
    "WARRIOR HAIR 2.png":,
    "WARRIOR HAIR 4.png":,
    "WARRIOR HAIR 3.png":
}
horn_names = {
    "WARRIOR HORN 3.png":,
    "WARRIOR HORN 2.png":,
    "WARRIOR HORN 4.png":,
    "WARRIOR HORN 1.png":
}
helmet_names = {
    "WARRIOR HELMET 1.png":,
    "WARRIOR HELMET 2.png":,
    "WARRIOR HELMET 3.png":,
    "WARRIOR HELMET 4.png":,
    "WARRIOR HELMET 5.png":,
    "WARRIOR HELMET 6.png":,
    "WARRIOR HELMET 7.png":,
    "WARRIOR HELMET 8.png":,
    "WARRIOR HELMET 9.png":
}
sword_names = {
    
}
accessory_names = {}







bCounter = 1

def whichBackground():
    n = random()
    if(n < 0.06):
        return "WARRIOR GRADIENT BACKGROUND 1.png"
    elif(n < 0.12):
        return "WARRIOR GRADIENT BACKGROUND 2.png"
    elif(n < 0.18):
        return "WARRIOR GRADIENT BACKGROUND 3.png"
    elif(n < 0.24):
        return "WARRIOR GRADIENT BACKGROUND 4.png"
    elif(n < 0.30):
        return "WARRIOR GRADIENT BACKGROUND 5.png"
    elif(n < 0.36):
        return "WARRIOR GRADIENT BACKGROUND 6.png"
    elif(n < 0.42):
        return "WARRIOR GRADIENT BACKGROUND 7.png"
    elif(n < 0.48):
        return "WARRIOR GRADIENT BACKGROUND 8.png"
    elif(n < 0.54):
        return "WARRIOR GRADIENT BACKGROUND 9.png"
    elif(n < 0.60):
        return "WARRIOR GRADIENT BACKGROUND 10.png"
    elif(n < 0.67):
        return "WARRIOR RARE BACKGROUND 1.png"
    elif(n < 0.73):
        return "WARRIOR RARE BACKGROUND 3.png"
    elif(n < 0.79):
        return "WARRIOR RARE BACKGROUND 4.png"
    elif(n < 0.895):
        return "WARRIOR RARE BACKGROUND 2.png"
    else:
        return "WARRIOR RARE BACKGROUND 5.png"
    
def whichBackWing():
    n = random()
    if(n < 0.2):
        return "WARRIOR BACK WING 1.png"
    elif(n < 0.4):
        return "WARRIOR BACK WING 2.png"
    elif(n < 0.6):
        return "WARRIOR BACK WING 3.png"
    elif(n < 0.8):
        return "WARRIOR BACK WING 4.png"
    else:
        return "WARRIOR BACK WING 5.png"
def whichTail():
    n = random()
    if(n < 0.28):
        return "WARRIOR TAIL 1.png"
    elif(n < 0.56):
        return "WARRIOR TAIL 2.png"
    elif(n < 0.85):
        return "WARRIOR TAIL 4.png"
    else:
        return "WARRIOR TAIL 3.png"

def whichBody():
    n = random()
    if(n < 0.3):
        return "WARRIOR BODY 4.png"
    elif(n < 0.6):
        return "WARRIOR BODY 6.png"
    elif(n < 0.75):
        return "WARRIOR BODY 1.png"
    elif(n < 0.90):
        return "WARRIOR BODY 3.png"
    elif(n < 0.95):
        return "WARRIOR BODY 7.png"
    else:
        return "WARRIOR BODY 8.png"

def whichEye():
    n = random()
    if(n < 0.04):
        return "WARRIOR EYE F1.png"
    elif(n < 0.08):
        return "WARRIOR EYE F2.png"
    elif(n < 0.12):
        return "WARRIOR EYE F3.png"
    elif(n < 0.16):
        return "WARRIOR EYE F4.png"
    elif(n < 0.20):
        return "WARRIOR EYE F5.png"
    elif(n < 0.36):
        return "WARRIOR EYE M1.png"
    elif(n < 0.52):
        return "WARRIOR EYE M2.png"
    elif(n < 0.68):
        return "WARRIOR EYE M3.png"
    elif(n < 0.84):
        return "WARRIOR EYE M4.png"
    else:
        return "WARRIOR EYE M5.png"


def whichHorn():
    n = random()
    if(n < 0.3):
        return "WARRIOR HORN 3.png"
    elif(n < 0.6):
        return "WARRIOR HORN 2.png"
    elif(n < 0.9):
        return "WARRIOR HORN 4.png"
    else:
        return "WARRIOR HORN 1.png"

def whichHelmet():
    n = random()
    if(n < 0.05):
        return "WARRIOR HELMET 1.png"
    elif(n < 0.18):
        return "WARRIOR HELMET 2.png"
    elif(n < 0.31):
        return "WARRIOR HELMET 3.png"
    elif(n < 0.43):
        return "WARRIOR HELMET 4.png"
    elif(n < 0.48):
        return "WARRIOR HELMET 5.png"
    elif(n < 0.61):
        return "WARRIOR HELMET 6.png"
    elif(n < 0.74):
        return "WARRIOR HELMET 7.png"
    elif(n < 0.87):
        return "WARRIOR HELMET 8.png"
    else:
        return "WARRIOR HELMET 9.png"
def whichSword():
    n = random()
    if(n < 0.07):
        return "WARRIOR SWORD 1.png"
    elif(n < 0.17):
        return "WARRIOR SWORD 2.png"
    elif(n < 0.27):
        return "WARRIOR SWORD 3.png"
    elif(n < 0.34):
        return "WARRIOR SWORD 4.png"
    elif(n < 0.4):
        return "WARRIOR SWORD 5.png"
    elif(n < 0.5):
        return "WARRIOR SWORD 6.png"
    elif(n < 0.6):
        return "WARRIOR SWORD 7.png"
    elif(n < 0.7):
        return "WARRIOR SWORD 8.png"
    elif(n < 0.8):
        return "WARRIOR SWORD 9.png"
    elif(n < 0.9):
        return "WARRIOR SWORD 10.png"
    else:
        return "WARRIOR SWORD 11.png"
def whichAccessory():
    n = random()
    if(n < 0.9):
        return "220329-0959-BOS LAYER.png"
    elif(n < 0.925):
        return "WARRIOR ACC 1.png"
    elif(n < 0.95):
        return "WARRIOR ACC 2.png"
    elif(n < 0.975):
        return "WARRIOR ACC 3.png"
    else:
        return "WARRIOR ACC 4.png"



Metadata = {}

while(bCounter < 2532):
    blessing = {}

    wBackground = whichBackground()
    images[0] = Image.open(backgrounds + "/" + wBackground).convert("RGBA")
    blessing["Background"] = background_names[wBackground]
    
    backW = whichBackWing()
    images[1] = Image.open(back_wings + "/" + backW).convert("RGBA")
    blessing["Back Wing"] = bWing_names[backW]

    wTail = whichTail()
    images[2] = Image.open(tail + "/" + wTail).convert("RGBA")
    blessing["Tail"] = tail_names[wTail]

    wBody = whichBody()
    images[3] = Image.open(bodies + "/" + wBody).convert("RGBA")
    blessing["Body"] = body_names[wBody]

    wEye = whichEye()
    images[4] = Image.open(eyes + "/" + wEye).convert("RGBA")
    blessing["Eyes"] = eye_names[wEye]

    #determining which front wing to use
    fWing = "WARRIOR FRONT WING " + backW[-5] + ".png"
    images[5] = Image.open(front_wings + "/" + fWing).convert("RGBA") #front wing
    blessing["Front Wing"] = fWing_names[fWing]
    
    #determining which hair to use
    wHair = "WARRIOR HAIR " + wTail[-5] + ".png"
    images[6] = Image.open(hair + "/" + wHair).convert("RGBA") #hair
    blessing["Hair"] = hair_names[wHair]

    wHorn = whichHorn()
    images[7] = Image.open(horn + "/" + wHorn).convert("RGBA")
    blessing["Horn"] = horn_names[wHorn]

    wHelmet = whichHelmet()
    images[8] = Image.open(helmets + "/" + wHelmet).convert("RGBA")
    blessing["Helmet"] = helmet_names[wHelmet]

    wSword = whichSword()
    images[9] = Image.open(sword + "/" + wSword).convert("RGBA")
    blessing["Sword"] = sword_names[wSword]

    wAccessory = whichAccessory()
    images[10] = Image.open(accessories + "/" + wAccessory).convert("RGBA")
    blessing["Accessory"] = accessory_names[wAccessory]

    final_image = images[0]

    #combining all layers
    for i in range(1,len(images)):
        final_image = Image.alpha_composite(final_image,images[i])
    #saving the image with the correct name and directory
    #print(str(bCounter) + " images generated")
    final_image.save(finalImages+"/Blessings Warrior " +str(bCounter)+".png")
    
    if(bCounter < 10):
        id = "Healer " + "000" + str(bCounter)
    elif(bCounter < 100):
        id = "Healer " + "00" + str(bCounter)
    elif(bCounter < 1000):
        id = "Healer "+ "0" + str(bCounter)
    else:
        id = str(bCounter)
    Metadata[id] = blessing
    
    bCounter += 1
