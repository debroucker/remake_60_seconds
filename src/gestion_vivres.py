# -*- coding: utf-8 -*-

def cachet_en_vie(liste_duree_vie_expedition):
	'''
	Renvoie True si les cahctes sont encore utilisables, False sinon

	:param liste_duree_vie_expedition: la liste de durée de vie de tous les
	objets utilisables en expédition
	:type liste_duree_vie_expedition: list
	:return: True ou False
	:rtype: bool
	'''
	compteur = 0
	copie = list(liste_duree_vie_expedition)
	while 'cachets' in copie :
		compteur += 1
		copie.remove('cachets')
	return compteur != 2





def vivres(liste_objet_prit_vivres, dico_vie_personnes, liste_objet_prit_abri, liste_objet_prit_autres, dico_objet_personnes, liste_duree_vie_expedition) :
	'''
	Gère la distribution des vivres : +10PV pour de l'eau, +5PV pour de la bouffe
	ou +10PV s'il y a un four dans l'abri

	:param liste_objet_prit_vivres: la liste des vivres (eau et bouffe)
	:type liste_objet_prit_vivres: list
	:param dico_vie_personnes: la vie de chaque personnes
	:type dico_vie_personnes: dict
	:param liste_objet_prit_abri: la liste des objets prit dans l'abri
	:type liste_objet_prit_abri: list
	:param liste_objet_prit_autres: la liste des autres objets prit dans l'abri
	(four, cachets, etc.)
	:type liste_objet_prit_autres: list
	:param dico_objet_personnes: les objets que le personnes auront sur eux
	(ex : maladie)
	:type dico_objet_personnes: dict
	:param liste_duree_vie_expedition: la durée des vie des objets utilisable
	en expédition (ex : le masque à gaz est utilisable 3 fois)
	:type liste_duree_vie_expedition: list
	'''
	if len(liste_objet_prit_vivres) == 0 : #s'il n'y a pas de vivres, on peut pas en donner
		print("tu n'as pas de vivres !")
		print()
		#gestion cahets
		for e in dico_objet_personnes :
			if not ('cachets' in liste_objet_prit_autres) and 'maladie' in dico_objet_personnes[e] : #pas de vires ni cachet et malade
				if e == 'fille' or e == 'femme' :
					print("ta", e, "est malade, mais tu n'as pas de cachet à lui donner !")
				else :
					print("ton", e, "est malade, mais tu n'as pas de cachet à lui donner !")
				print()

			if 'cachets' in liste_objet_prit_autres and 'maladie' in dico_objet_personnes[e] :  #pas de vires mais cachet et malade
				if e == 'fille' or e == 'femme' :
					print("ta", e, "est malade")
				else :
					print("ton", e, "est malade")
				print()
				print("veux-tu lui donner un cachet?")
				choix = input("'oui' ou 'non' : ")
				#assert
				while choix not in ['oui', 'non'] :
					print("SAISIR 'oui' OU 'non' !")
					choix = input("'oui' ou 'non' : ")
				if choix == 'oui' :
					print()
					liste_duree_vie_expedition.append('cachets')
					if e == 'fille' or e == 'femme' :
						print("tu as donné un cachet à ta", e)
						print("elle est donc guérie")
						print()
						while 'maladie' in (dico_objet_personnes[e]) :
							dico_objet_personnes[e].remove('maladie')
					else :
						print("tu as donné un cachet à ton", e)
						print("il est donc guéri")
						print()
						while 'maladie' in (dico_objet_personnes[e]) :
							dico_objet_personnes[e].remove('maladie')

					#tjrs des cachets?
					if not cachet_en_vie(liste_duree_vie_expedition) :
						print("tu as utilisé tous les cachets de cette trousse !")
						print()
						while 'cachets' in liste_duree_vie_expedition :
							liste_duree_vie_expedition.remove('cachets')
						liste_objet_prit_abri.remove('cachets')
						liste_objet_prit_autres.remove('cachets')

	#distribution de vivres
	else :
		for e in dico_vie_personnes :
			if dico_vie_personnes[e] >= 100 : #vie pleine, pas de vivre
				if e == 'fille' or e == 'femme' :
					print("ta", e, "a sa vie pleine, tu ne peux pas lui donner de vivres")
				else :
					print("ton", e, "a sa vie pleine, tu ne peux pas lui donner de vivres")
				print()
				print("========")
				print()

			#s'il est en vie et qu'il y a des vivres disponibles
			if 100 > dico_vie_personnes[e] > 0 :
				#affichage
				print("tu as comme vivres : ",end='')
				for i in range(len(liste_objet_prit_vivres)) :
					if i % 5 == 0 :
						print()
						if i == len(liste_objet_prit_vivres) -1 :
							print(liste_objet_prit_vivres[i], end = '')
						else :
							print(liste_objet_prit_vivres[i], end = ', ')
					elif i == len(liste_objet_prit_vivres) -1 :
						print(liste_objet_prit_vivres[i], end = '')
					else :
						print(liste_objet_prit_vivres[i], end = ', ')
				print()
				print()

				#gestion cachets
				if 'maladie' in dico_objet_personnes[e] :
					if not ('cachets' in liste_objet_prit_autres) :
						if e == 'fille' or e == 'femme' :
							print("ta", e, "est malade, mais tu n'as pas de cachet à lui donner !")
						else :
							print("ton", e, "est malade,  mais tu n'as pas de cachet à lui donner !")
						print()
					else :
						if e == 'fille' or e == 'femme' :
							print("ta", e, "est malade")
						else :
							print("ton", e, "est malade")
						print()
						print("veux-tu lui donner un cachet?")
						choix = input("'oui' ou 'non' : ")
						#assert
						while choix not in ['oui', 'non'] :
							print("SAISIR 'oui' OU 'non' !")
							choix = input("'oui' ou 'non' : ")
						if choix == 'oui' :
							print()
							liste_duree_vie_expedition.append('cachets')
							if e == 'fille' or e == 'femme' :
								print("tu as donné un cachet à ta", e)
								print("elle est donc guérie")
								print()
								while 'maladie' in (dico_objet_personnes[e]) :
									dico_objet_personnes[e].remove('maladie')
							else :
								print("tu as donné un cachet à ton", e)
								print("il est donc guéri")
								print()
								while 'maladie' in (dico_objet_personnes[e]) :
									dico_objet_personnes[e].remove('maladie')

							#tjrs des cachets?
							if not cachet_en_vie(liste_duree_vie_expedition) :
								print("tu n'as plus de cachet !")
								print()
								while 'cachets' in liste_duree_vie_expedition :
									liste_duree_vie_expedition.remove('cachets')
								liste_objet_prit_abri.remove('cachets')
								liste_objet_prit_autres.remove('cachets')


				if e == 'fille' or e == 'femme' :
					print("veux-tu donner des vivres à ta", e, "?")
				else :
					print("veux-tu donner des vivres à ton", e, "?")
				choix = input("'oui' ou 'non' : ")
				#assert
				while choix not in ['oui', 'non'] :
					print("SAISIR 'oui' OU 'non' !")
					choix = input("'oui' ou 'non' : ")

				while choix == 'oui' and 100 > dico_vie_personnes[e] > 0 and len(liste_objet_prit_vivres) != 0 :
					print()
					print("que veux-tu donner?")
					choix_vivres = input("'bouffe' ou 'eau' : ")
					#assert
					while choix_vivres not in liste_objet_prit_vivres :
						print("SAISIR 'bouffe' OU 'eau' !")
						choix_vivres = input("'bouffe' ou 'eau' : ")
					while choix_vivres not in liste_objet_prit_vivres :
						print("SAISIR UN VIVRE DISPONIBLE !")
						choix_vivres = input("'bouffe' ou 'eau' : ")

					if choix_vivres == 'bouffe' :
						if 'four' in liste_objet_prit_abri :
							dico_vie_personnes[e] += 10 #+10PV pour la bouffe chaude
						else :
							dico_vie_personnes[e] += 5 #+5PV pour la bouffe
					elif choix_vivres == 'eau' :
						dico_vie_personnes[e] += 10 #+10PV pour de l'eau
					liste_objet_prit_vivres.remove(choix_vivres)
					liste_objet_prit_abri.remove(choix_vivres)

					#et que le perso n'est pas plus de 100PV
					if dico_vie_personnes[e] >= 100 :
						print()
						choix = 'non'

					elif dico_vie_personnes[e] < 100 and len(liste_objet_prit_vivres) != 0 :
						#affichage
						print()
						print("tu as comme vivres : ",end='')
						for i in range(len(liste_objet_prit_vivres)) :
							if i % 5 == 0 :
								print()
								if i == len(liste_objet_prit_vivres) -1 :
									print(liste_objet_prit_vivres[i], end = '')
								else :
									print(liste_objet_prit_vivres[i], end = ', ')
							elif i == len(liste_objet_prit_vivres) -1 :
								print(liste_objet_prit_vivres[i], end = '')
							else :
								print(liste_objet_prit_vivres[i], end = ', ')
						print()
						print()
						print("====")
						print()
						print("veux-tu redonner des vivres à ce personnage ?")
						choix = input("'oui' ou 'non' : ")
						#assert
						while choix not in ['oui', 'non'] :
							print("SAISIR 'oui' OU 'non' !")
							choix = input("'oui' ou 'non' : ")

					if len(liste_objet_prit_vivres) == 0: #s'il n'y a pas de vivres, on peut pas en donner
						print()
						print("====")
						print()
						print("tu n'as plus de vivres !")

					if dico_vie_personnes[e] >= 100 :
						print()
						print("====")
						print()
						print("ce personnage a sa vie pleine grace au vivres que tu lui a donné")

				print()
				print("========")
				print()

		#si le perso a plus de 100PV, on les remet a 100 (ex : perso a 95PV, il rentre dans la boucle, et on lui donne de l'eau, donc +10PV)
		if dico_vie_personnes[e] > 100 :
			dico_vie_personnes[e] = 100