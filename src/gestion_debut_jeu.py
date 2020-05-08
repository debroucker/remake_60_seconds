# -*- coding: utf-8 -*-
import random
import time

def debut_jeu(s) :
	'''
	lance le début du jeu : la saisie d'objets dans la maison

	:param s: le nombre de seconde où l'on peut prendre des objets dans le maison
	:type s: int
	:return: la liste des objets prit dans l'abri, et la durée de vie des objets
	utilisable dans les expéditions (ex : le masque à gaz est utilisable 3 fois)
	:rtype: tuple (de deux listes)
	'''
	#initialisation
	liste_objet_maison = ['bouffe' for i in range(8)] +  ['eau' for i in range(7)]
	liste_objet_maison += ['fils', 'fille', 'femme', 'sac', 'masque à gaz', 'four', 'fusil', 'cachets'] #liste des objets dans la maison
	random.shuffle(liste_objet_maison)
	liste_objet_prit_temp = [] #liste des objets que le perso a sur lui
	liste_objet_prit_abri = [] #liste des objets que le perso a dans son abri

	#saisie des objets
	fin = time.time() + s #l'heure actuelle + les seconde(s) voulue(s)
	while time.time() < fin and len(liste_objet_maison) != 0 : #tant que le temps est pas dépassé ou que le perso n'a pas tout prit dans la maison

		#affichage
		print("voici la liste des objets que tu as dans ta maison : ", end ='')
		for i in range(len(liste_objet_maison)) :
			if i % 5 == 0 :
				print()
				if  i == len(liste_objet_maison) -1 :
					print(liste_objet_maison[i], end = '')
				else :
					print(liste_objet_maison[i], end = ', ')
			elif i == len(liste_objet_maison) -1 :
				print(liste_objet_maison[i], end = '')
			else :
				print(liste_objet_maison[i], end = ', ')
		print()
		print()

		objet_prit = input("saisir un objet dans la liste d'objet disponible : ")
		#assert
		while objet_prit not in liste_objet_maison :
			print("saisir un objet valide !")
			objet_prit = input("saisir un objet dans la liste d'objet disponible : ")
		liste_objet_prit_temp.append(objet_prit)
		liste_objet_maison.remove(objet_prit)
		#si perso prend le sac, il peut prendre 7 objets sur lui (en plus du sac) avant de les deposer dans son abri
		#sinon, il ne peut en prendre que 3
		if 'sac' in liste_objet_prit_temp :
			remplie = 7
		elif 'sac' not in liste_objet_prit_temp :
			remplie = 3
		#si le perso a trop d'objet sur lui, il doit les mettres dans son abri
		if len(liste_objet_prit_temp) == remplie :
			liste_objet_prit_abri += liste_objet_prit_temp
			#si le perso a prit la sac, il le garde sur lui
			if 'sac' in liste_objet_prit_temp :
				liste_objet_prit_temp = ['sac']
				liste_objet_prit_abri.remove('sac') #pour pas qu'il y est plusieurs fois le sac
			elif 'sac' not in liste_objet_prit_temp :
				liste_objet_prit_temp = []
			print()
			print("ton perso doit mettre les objets qu'il a prit dans son abri...")
			for i in range(2,0,-1) :
				print(i)
				time.sleep(1)

		if fin - time.time() > 0 :
			print("il reste", round(fin - time.time(), 2), "secondes")
		print()
		print("======================")
		print()

	#gestion à la fin du temps impartis
	liste_objet_prit_abri += liste_objet_prit_temp
	print("tu as prit : ", end = '')
	for i in range(len(liste_objet_prit_abri)) :
		if i % 5 == 0 :
			print()
			if  i == len(liste_objet_prit_abri) -1 :
				print(liste_objet_prit_abri[i], end = '')
			else :
				print(liste_objet_prit_abri[i], end = ', ')
		elif i == len(liste_objet_prit_abri) -1 :
			print(liste_objet_prit_abri[i], end = '')
		else :
			print(liste_objet_prit_abri[i], end = ', ')
	print()
	print()
	print("======================")
	print()
	#inisialisation de liste_duree_vie_expedition (utile pour masque à gaz, fusil)
	liste_duree_vie_expedition = []
	return liste_objet_prit_abri, liste_duree_vie_expedition