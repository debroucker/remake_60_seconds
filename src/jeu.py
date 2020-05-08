# -*- coding: utf-8 -*-
import time
import random

import gestion_debut_jeu
import gestion_expeditions
import gestion_surprises
import gestion_vies
import gestion_vivres

temps = 35
temps_bis = 5

def jeux(s,a) :
	'''
	Lance le jeu "remake_60_secondes" : une bombe nucléaire va explsée et on a
	s secondes (passé en paramètres) pour rassembler un maximum d'objets présent
	dans la maison. Le but est ensuite de survivre le plus longtemps possible

	:param s: le nombre de seconde pour prendre les objets dans la maison
	:type s: int
	:param a: le nombre de seconde avant que le jeu ne démarre après avoir lancé
	le programme
	:param a: int
	'''

	print("========== REMAKE DU JEU '60 SECONDES' ========== ")
	print()
	print()
	print("TU VAS AVOIR", s, "SECONDES POUR RECUPERER DES OBJETS...")
	print()
	print()
	print("DEBUT DE PARTIE DANS...")
	for i in range(a,0,-1) :
		print(i)
		time.sleep(1)
	print("JOUE ! ")
	print()
	print()
	print("======================")
	print()

	jour_survie = 1
	partie = gestion_debut_jeu.debut_jeu(s)
	partie_objet = partie[0]
	partie_duree_vie_expedition = partie[1]
	depart = gestion_vies.vie_personnes_initialisation(partie_objet)
	vie_depart = depart[0]
	objet_depart = depart[1]
	jour_surprise = random.randint(2,5) #jour ou qqun toc a la porte de l'abri
	print()
	print()

	while True :
		#differencie les listes
		gestion_objets = gestion_expeditions.gestion_objets_prits(partie_objet)
		liste_vivres = gestion_objets[0]
		liste_utilisable_expedition = gestion_objets[1]
		liste_autres = gestion_objets[2]

		print("==============================")
		print("==============================")
		print()
		print("DEBUT DU JOUR", jour_survie)
		print()
		print()

		print("=============VIES=============")
		print()
		gestion_vies.vie_personnes(vie_depart)
		print()

		#verification
		if not gestion_vies.en_vie(vie_depart) :
			print()
			print("==============================")
			print()
			print("PERDU, TOUTES LES PERSONNES SONT MORTES")
			print("TU AS SURVECU",jour_survie, "JOURS")
			print()
			print("==============================")
			print()
			break

		print("==========EXPEDITION==========")
		print()
		gestion_expeditions.expedition(partie_objet, vie_depart, objet_depart, liste_utilisable_expedition, partie_duree_vie_expedition)

		print("=============VIES=============")
		print()
		gestion_vies.affichage_vie(vie_depart)
		print()

		#differencie les listes
		gestion_objets = gestion_expeditions.gestion_objets_prits(partie_objet)
		liste_vivres = gestion_objets[0]
		liste_utilisable_expedition = gestion_objets[1]
		liste_autres = gestion_objets[2]

		#verification
		if not gestion_vies.en_vie(vie_depart) :
			print()
			print("==============================")
			print()
			print("PERDU, TOUTES LES PERSONNES SONT MORTES")
			print("TU AS SURVECU",jour_survie, "JOURS")
			print()
			print("==============================")
			print()
			break

		#surprise
		if jour_survie == jour_surprise :
			print("===========SURPRISE===========")
			print()
			gestion_surprises.surprise(partie_objet)
			print()
			jour_surprise = random.randint(jour_survie+2, jour_survie+5)
			#differencie les listes
			gestion_objets = gestion_expeditions.gestion_objets_prits(partie_objet)
			liste_vivres = gestion_objets[0]
			liste_utilisable_expedition = gestion_objets[1]
		liste_autres = gestion_objets[2]

		print("============VIVRES============")
		print()
		gestion_vivres.vivres(liste_vivres, vie_depart, partie_objet, liste_autres, objet_depart, partie_duree_vie_expedition)

		print("=============VIES=============")
		print()
		gestion_vies.affichage_vie(vie_depart)

		print()
		print("==============================")
		print()
		print("FIN DU JOUR", jour_survie)
		print()
		print("==============================")
		print("==============================")
		print()
		print()
		jour_survie += 1


jeux(temps,temps_bis)