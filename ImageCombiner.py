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




while(bCounter < 2532):
    images[0] = Image.open(backgrounds + "/" + whichBackground()).convert("RGBA")
    backW = whichBackWing()
    images[1] = Image.open(back_wings + "/" + backW).convert("RGBA")
    wTail = whichTail()
    images[2] = Image.open(tail + "/" + wTail).convert("RGBA")
    images[3] = Image.open(bodies + "/" + whichBody()).convert("RGBA")
    images[4] = Image.open(eyes + "/" + whichEye()).convert("RGBA")
    #determining which front wing to use
    fWing = "WARRIOR FRONT WING " + backW[-5] + ".png"
    images[5] = Image.open(front_wings + "/" + fWing).convert("RGBA") #front wing
    #determining which hair to use
    wHair = "WARRIOR HAIR " + wTail[-5] + ".png"
    images[6] = Image.open(hair + "/" + wHair).convert("RGBA") #hair
    images[7] = Image.open(horn + "/" + whichHorn()).convert("RGBA")
    images[8] = Image.open(helmets + "/" + whichHelmet()).convert("RGBA")
    images[9] = Image.open(sword + "/" + whichSword()).convert("RGBA")
    images[10] = Image.open(accessories + "/" + whichAccessory()).convert("RGBA")
    final_image = images[0]

    #combining all layers
    for i in range(1,len(images)):
        final_image = Image.alpha_composite(final_image,images[i])
    #saving the image with the correct name and directory
    print(str(bCounter) + " images generated")
    final_image.save(finalImages+"/Blessings Warrior " +str(bCounter)+".png")
    bCounter += 1
