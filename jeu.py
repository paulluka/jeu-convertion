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
		reponse = "Correct. Félicitation !"
		generation(new_level)
		afficher_octet.config(text=generation_binaire)
	else:
		reponse = "Hmmm... le résultat n'est pas celui la !"

	saisie_decimal.delete(0, END)
	

	
	#-----------------------------------
	#création fenetre reponse
	#-----------------------------------		

	interface_reponse = Tk()
	interface_reponse.geometry("250x50")
	interface_reponse.title("Resultat !")

	phrase_reponse = Label(interface_reponse, text=reponse)
	phrase_reponse.grid(row=0, column=1)
	
	boutton_quitter_reponse = Button(interface_reponse, text="Recommencer", command=interface_reponse.destroy)
	boutton_quitter_reponse.grid(row=0, column=3)
	

	

	interface_reponse.mainloop()





		

#------------------------------------------------------------------------------------------------
#Création de l'interface graphique																#
#------------------------------------------------------------------------------------------------
generation(1)

# Premiere fenetre interface_insertion
interface_insertion = Tk()
interface_insertion.geometry("500x110")
interface_insertion.title("Convertion d'un nombre binaire")

# text de l'octet
text_afficher_octet = Label(interface_insertion, text="Convertir l'octet  : ")
text_afficher_octet.grid(row=0, column=0)

#afficher l'octet
afficher_octet = Label(interface_insertion, text =generation_binaire)
afficher_octet.grid(row=0, column=1)

def update_level(x):
	global new_level
	new_level = x
	print(new_level)

#scale
scale_text = Label(interface_insertion, text ="Choisissez un niveau entre 1 et 3 suivant votre niveau.")
scale_text.grid(row=1, column=0)

scale_level = Scale(interface_insertion, from_=1,to=3, orient=HORIZONTAL , command= update_level)
scale_level.grid(row=1, column=1)


#text decimal
saisie_text_decimal = Label(interface_insertion, text="La valeur decimal est : ")
saisie_text_decimal.grid(row=2, column=0)

#saisir decimal
saisie_decimal = Entry(interface_insertion)
saisie_decimal.grid(row=2, column=1)

#Boutton de validataion 
boutton_valider = Button(interface_insertion, text="Valider", command=verify)
boutton_valider.grid(row=3, column=0)



#boutton quitter
boutton_quitter = Button(text="Quitter", command=interface_insertion.destroy)
boutton_quitter.grid(row=3, column=1)

scale_level.set(2)
scale_level.set(1)


interface_insertion.mainloop()

#--------------------------------------------------------------

