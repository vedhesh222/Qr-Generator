#Importing the Modules
import qrcode
from art import *
import os

#Art Work
art = text2art("Qr Generator")
print(art)

#Getting the Inputs
dre = input("Enter the Directory: ")
dat = input("Enter the Data here: ")
nam = input("Enter the Name for your QrCode with Formate: ")
fgc = input("Enter the Foreground Color: ")
bgc = input("Enter the Backgroung color: ")
ver = int(input("Enter the Qr Version: "))
bos = int(input("Enter the Box size: "))
bor = int(input("Enter the Border: "))

#Changing the Directory
os.chdir(dre)

#Working with it
qr = qrcode.QRCode(version = ver, box_size = bos , border = bor )
qr.add_data(dat)
img = qr.make_image(fill_color = fgc, back_color = bgc)
img.save(nam)

#Result
print('')
print("Done your Qr is saved at", dre)
print('')
closing = input("Hit 'Enter' to Exit...")
