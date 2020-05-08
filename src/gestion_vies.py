# -*- coding: utf-8 -*-

perte_journaliere_vie_parent = 10
perte_journaliere_vie_enfant = 15

def vie_personnes_initialisation(liste_objet_prit_abri) :
	'''
	Initialise la vie des personnes (ex :si le joueur a prit sa femme, elle a
	100PV, sinon elle est mort est donc a 0PV)

	:param liste_objet_prit_abri : la liste des objets prit dans l'abri
	(comme précédemment)
	:type liste_objet_prit_abri: list
	:return: le dictionnaire de la vie des personnages, et le dictionnaire
	des "objets" qu'ils ont (ex : maladie)
	:rtype: tuple (de deux dictionnaires)
	'''
	#dico_vie_personnes
	vie_femme = vie_fille = vie_fils = 0
	vie_perso = 100 + perte_journaliere_vie_parent
	#si le perso a prit des persoones, ils ont 100PV, sinon 0
	if 'fille' in liste_objet_prit_abri :
		vie_fille = 100 + perte_journaliere_vie_enfant
		liste_objet_prit_abri.remove('fille') #on en a plus besoin
	if 'fils' in liste_objet_prit_abri :
		vie_fils = 100 + perte_journaliere_vie_enfant
		liste_objet_prit_abri.remove('fils') #on en a plus besoin
	if 'femme' in liste_objet_prit_abri :
		vie_femme = 100 + perte_journaliere_vie_parent
		liste_objet_prit_abri.remove('femme') #on en a plus besoin
	dico_vie_personnes = {'perso' : vie_perso, 'femme' : vie_femme, 'fille' : vie_fille, 'fils' : vie_fils}

	#affichage
	for e in dico_vie_personnes :
		if e == 'perso' :
			print("ton " + str(e) + " a " + str(dico_vie_personnes[e]-perte_journaliere_vie_parent) + "PV")
		elif e == 'femme' :
			if dico_vie_personnes[e] == 0:
				print("tu as oublié ta " + str(e) + ", par conséquent elle est morte")
			else :
				print("ta " + str(e) + " a " + str(dico_vie_personnes[e]-perte_journaliere_vie_parent) + "PV")
		elif e == 'fille' :
			if dico_vie_personnes[e] == 0:
				print("tu as oublié ton " + str(e) + ", par conséquent elle est morte")
			else :
				print("ta " + str(e) + " a " + str(dico_vie_personnes[e]-perte_journaliere_vie_enfant) + "PV")
		elif e == 'fils' :
			if dico_vie_personnes[e] == 0:
				print("tu as oublié ton " + str(e) + ", par conséquent il est mort")
			else :
				print("ta " + str(e) + " a " + str(dico_vie_personnes[e]-perte_journaliere_vie_enfant) + "PV")
		print()
	print("======================")

	#dico_objet_personnes initialisation
	dico_objet_personnes = {'perso' : [], 'femme' : [], 'fille' : [], 'fils' : []}
	return dico_vie_personnes, dico_objet_personnes




def vie_personnes(dico_vie_personnes):
	'''
	Diminue la vie des personnes chaque jours

	:param dico_vie_personnes: la vie de chaque personnes
	:type dico_vie_personnes: dict
	'''
	for e in dico_vie_personnes :
		if e == 'fille' or e == 'fils' :
			dico_vie_personnes[e] -= perte_journaliere_vie_enfant #un gosse = plus fragile = perd plus de vie par jour
		else :
			dico_vie_personnes[e] -= perte_journaliere_vie_parent
		if dico_vie_personnes[e] <= 0 :
			if e == 'fille' or e == 'femme' :
				print("ta", e, "est morte")
			else :
				print("ton", e, "est mort")
		else :
			if e == 'fille' or e == 'femme' :
				print("ta " + str(e) + " a " + str(dico_vie_personnes[e]) + "PV")
			else :
				print("ton " + str(e) + " a " + str(dico_vie_personnes[e]) + "PV")
		print()




def affichage_vie(dico_vie_personnes) :
	'''
	Pour gerer l'affichage des vie des personnes

	:param dico_vie_personnes: la vie de chaque personnes
	:type dico_vie_personnes: dict
	'''
	for e in dico_vie_personnes :
		if dico_vie_personnes[e] <= 0 :
			if e == 'fille' or e == 'femme' :
				print("ta", e, "est morte")
			else :
				print("ton", e, "est mort")
		else :
			if e == 'fille' or e == 'femme' :
				print("ta " + str(e) + " a " + str(dico_vie_personnes[e]) + "PV")
			else :
				print("ton " + str(e) + " a " + str(dico_vie_personnes[e]) + "PV")
		print()



def en_vie(dico_vie_personnes) :
	'''
	Retourne True si au moins un des personnages et en vie

	:param dico_vie_personnes: la vie de chaque personnes
	:type dico_vie_personnes: dict
	:return: True ou False
	:rtype: bool
	'''
	liste_personnes_en_vie = []
	for e in dico_vie_personnes :
		if dico_vie_personnes[e] <= 0 :
			liste_personnes_en_vie.append('mort')
		else :
			liste_personnes_en_vie.append('vivant')
	return 'vivant' in liste_personnes_en_vie