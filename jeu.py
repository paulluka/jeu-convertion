#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jeu.py
#  Paul Lukasiewicz et Ilyess Boussif

#import des modules
from tkinter import * # interface graphique
import random
#------------------------------------------------------------------------------------
def generation(level):
	"""
		Creer un octet a partit d'un decimal aléatoire
		Level sert a choisir le niveau (globale type int)
		retourne une valeure en binaire
		generation_decimal globale
	"""
	global generation_binaire
	global generation_decimal
	if int(level) == 1:
		generation_decimal = random.randint(0, 15)
	elif int(level) == 2:
		generation_decimal = random.randint(16, 254)
	elif int(level) == 3:
		generation_decimal = random.randint(255, 65535)

	generation_binaire = bin(generation_decimal)[2:]
	print(generation_decimal)


def verify():

	if saisie_decimal.get() == str(generation_decimal):
		print("c bn chakal")
		generation(new_level)
	else:
		print("c ps bon ça")

	saisie_decimal.delete(0, END)



		

#------------------------------------------------------------------------------------------------
#Création de l'interface graphique																#
#------------------------------------------------------------------------------------------------
generation(2)

# Premiere fenetre interface_insertion
interface_insertion = Tk()
interface_insertion.geometry("300x110")
interface_insertion.title("Convertion d'un nombre binaire")

# text de l'octet
text_afficher_octet = Label(interface_insertion, text="converti l'octet  : ")
text_afficher_octet.grid(row=0, column=0)

#afficher l'octet
afficher_octet = Label(interface_insertion, text ="Octet")
afficher_octet.grid(row=0, column=1)

def update_level(x):
	global new_level
	new_level = x

#scale
scale_text = Label(interface_insertion, text ="choisissez un niveau")
scale_text.grid(row=1, column=0)

scale_level = Scale(interface_insertion, from_=1,to=3, orient=HORIZONTAL , command= update_level)
scale_level.grid(row=1, column=1)


#text decimal
saisie_text_decimal = Label(interface_insertion, text="la valeur decimal est : ")
saisie_text_decimal.grid(row=2, column=0)

#saisir decimal
saisie_decimal = Entry(interface_insertion)
saisie_decimal.grid(row=2, column=1)

#Boutton de validataion 
boutton_valider = Button(interface_insertion, text="valider", command=verify)
boutton_valider.grid(row=3, column=0)


#boutton quitter
boutton_quitter = Button(text="Quitter", command=interface_insertion.destroy)
boutton_quitter.grid(row=3, column=1)

interface_insertion.mainloop()
