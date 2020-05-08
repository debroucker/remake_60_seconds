# -*- coding: utf-8 -*-
import random
import time

perte_journaliere_vie_parent = 10
perte_journaliere_vie_enfant = 15

def gestion_objets_prits(liste_objet_prit_abri) :
	'''
	Separe les objets prit dans l'abri en plusieurs catégories : les vivres,
	les objets utilisable en expédition, et autre (ex : four)

	:param liste_objet_prit_abri: la liste des objets prit dans l'abri
	:type liste_objet_prit_abri: list
	:return: les listes triées par catégories
	:rtype: tuple (de trois listes)
	'''
	liste_objet_prit_vivres = [] #on met que bouffe et eau
	liste_objet_prit_utilisable_expedition = [] #on met fusil, masque à gaz et sac
	liste_objet_prit_autres = [] #on met le reste
	for e in liste_objet_prit_abri :
		if e == 'bouffe' or e == 'eau' :
			liste_objet_prit_vivres.append(e)
		elif e == 'sac' or e == 'masque à gaz' or e == 'fusil' :
			liste_objet_prit_utilisable_expedition.append(e)
		else : #four et cachets
			liste_objet_prit_autres.append(e)
	return liste_objet_prit_vivres, liste_objet_prit_utilisable_expedition, liste_objet_prit_autres




def expedition(liste_objet_prit_abri, dico_vie_personnes, dico_objet_personnes, liste_objet_prit_utilisable_expedition, liste_duree_vie_expedition):
	'''
	Gère les expédition : une personne par jour, si la personne prends des objets
	(fusil, sac, etc.). Gère ce qu'il se passe durant l'expédition (si la personne
	se fait attaqué, tombe malade, ramèene des objets ou non si elle meurt etc.)

	:param liste_objet_prit_abri: la liste des objets prit dans l'abri
	:type liste_objet_prit_abri: list
	:param dico_vie_personnes: la vie des personnes
	:type dico_vie_personnes: dict
	:param dico_objet_personnes: les objets que le personnes auront sur eux
	(ex : maladie)
	:type dico_objet_personnes: dict
	:param liste_objet_prit_utilisable_expedition: la liste des objets utilisable
	en expédition
	:type liste_objet_prit_utilisable_expedition: list
	:param liste_duree_vie_expedition: la durée de vie des objets utilisable
	en expédition (ex : le masque à gaz est utilisable 3 fois)
	:type liste_duree_vie_expedition: list
	'''
	liste_objet_prit_expedition = [] #liste objets trouvé en expédition
	#affichage
	if len(liste_objet_prit_abri) == 0 :
		print("tu n'as plus rien dans ton abri !", end='')

	elif len(liste_objet_prit_abri) != 0 :
		print("tu as dans ton abri : ", end='')
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

	#personne qui peut partir (en vie et pas malade)
	choix_valide_personne = []
	for e in dico_vie_personnes :
		if dico_vie_personnes[e] > 0 and 'maladie' not in dico_objet_personnes[e] :
			choix_valide_personne.append(e)

	#expédition ?
	if len(choix_valide_personne) == 0 :
		print("personne ne peut partir en expédition")
		choix = 'non'
	else :
		print("veux-tu partir en expédition aujourd'hui ?")
		choix = input("'oui' ou 'non' : ")
		#assert
		while choix not in ['oui', 'non'] :
			print("SAISIR 'oui' OU 'non' !")
			choix = input("'oui' ou 'non' : ")
		print()

	if choix == 'oui' : #une personne part
		for e in dico_vie_personnes :
			if dico_vie_personnes[e] > 0 : #si vivant
				if 'maladie' in dico_objet_personnes[e] : #si malade, peut pas partir en expédition
					if e == 'fille' or e == 'femme' :
						print("ta", e, "ne peut pas partir en expédition, elle est malade")
					else :
						print("ton", e, "ne peut pas partir en expédition, il est malade")
					print()
					est_malade(e, dico_vie_personnes) #baisse sa vie
					dico_objet_personnes[e].remove('maladie') #il est malade 3 jours


		print("il n'y a qu'une personne qui peut partir en expédition par jour")
		print("tu peux choisir : ", end='')
		for i in range(len(choix_valide_personne)) :
			if i == len(choix_valide_personne) -1 :
				print(choix_valide_personne[i], end = '')
			else :
				print(choix_valide_personne[i], end = ', ')
		print()

		choix_personne = input("choisis une personne disponible: ")
		#assert
		while choix_personne not in choix_valide_personne :
			print("SAISIR UNE PERSONNE VALIDE !")
			choix_personne = input("choisis une personne disponible: ")
		print()

		#objets ?
		if len(liste_objet_prit_utilisable_expedition) == 0:
			print("tu n'as pas d'objet que tu pourrais prendre pour l'expédition")
		else :
			#choix objet pour expédition
			print("veux-tu prendre un objet pour l'expédition? ")
			choix_bis = input("'oui' ou 'non' : ")
			#assert
			while choix_bis not in ['oui', 'non'] :
				print("SAISIR 'oui' OU 'non' !")
				choix_bis = input("'oui' ou 'non' : ")
			print()
			if choix_bis == 'oui' : #prends des objets
				print("tu peux prendre : ", end='')
				#affichage
				for i in range(len(liste_objet_prit_utilisable_expedition)) :
					if i % 5 == 0 :
						print()
						if  i == len(liste_objet_prit_utilisable_expedition) -1 :
							print(liste_objet_prit_utilisable_expedition[i], end = '')
						else :
							print(liste_objet_prit_utilisable_expedition[i], end = ', ')
					elif i == len(liste_objet_prit_utilisable_expedition) -1 :
						print(liste_objet_prit_utilisable_expedition[i], end = '')
					else :
						print(liste_objet_prit_utilisable_expedition[i], end = ', ')

				print()
				choix_objet = input("choisis un objet disponible : ")
				#asert
				while choix_objet not in liste_objet_prit_utilisable_expedition :
					print("SAISIR UN OBJET VALIDE !")
					choix_objet = input("choisis un objet disponible : ")
				print()
				liste_objet_prit_expedition.append(choix_objet)
				liste_objet_prit_abri.remove(choix_objet)
				if choix_objet != 'fusil' : #le fuisl baisse en durée de vie seulement s'il le perso se fait attaqué
					liste_duree_vie_expedition.append(choix_objet)


		######expédition#######

		#liste des objets qu'on peut trouver en expédition
		liste_expedition = ['bouffe' for i in range(12)] + ['eau' for i in range(10)] + ['sac' for i in range(2)] + ['four' for i in range(1)]
		liste_expedition += ['fusil' for i in range(1)] + ['cachets' for i in range(1)] + ['masque à gaz' for i in range(1)]
		random.shuffle(liste_expedition)

		#sac ou pas?
		if 'sac' in liste_objet_prit_expedition :
			hasard = random.randint(0,6)
			for i in range(hasard): #s'il a le sac sur lui, il peut prendre 7 objets (+ le sac) dont 6 que de vivres et d'objets
				liste_objet_prit_expedition.append(liste_expedition[0])
				liste_expedition.remove(liste_expedition[0])

		elif 'sac' not in liste_objet_prit_expedition :
			hasard = random.randint(0,2)
			for i in range(hasard) :  #sinon, il peut en prendre que 3 dont 2 que de vivres et d'objets
				liste_objet_prit_expedition.append(liste_expedition[0])
				liste_expedition.remove(liste_expedition[0])

		#ajout de suplément (maladie, etc)
		#on l'ajoute ici, car si joueur a un sac, il a plus de chance d'avoir la maladie etc qu'un joueur sans sac => injuste
		liste_expedition += ['maladie' for i in range(6)] + ['attaque' for i in range(6)] + ['vol' for i in range(6)]
		random.shuffle(liste_expedition)

		#masque à gaz?
		if 'masque à gaz' in liste_objet_prit_expedition :
			while 'maladie' in liste_expedition :
				liste_expedition.remove('maladie') #on enleve 'maladie' comme ça il tombe plus malade

		#fusil ?
		if 'fusil' in liste_objet_prit_expedition :
			liste_expedition.remove('attaque') #on enleve 1 'attaque', il a moins de chance de se faire attaquer

		liste_objet_prit_expedition.append(liste_expedition[0]) #ajout d'autres objets (vivres, objets mais aussi malus)

		#attente de l'expedition
		if choix_personne == 'fille' or choix_personne == 'femme' :
			print("ta", choix_personne, "est partie en expédition...")
		else :
			print("ton", choix_personne, "est partit en expédition...")
		for i in range(5,0,-1) :
			print(i)
			time.sleep(1)

		#gestion maladie :
		if 'maladie' in liste_objet_prit_expedition :
			print()
			affichage_malade(choix_personne, dico_vie_personnes)
			est_malade(choix_personne, dico_vie_personnes)
			liste_objet_prit_expedition.remove('maladie')
			dico_objet_personnes[choix_personne] += ['maladie' for i in range(2)]  #il est malade 3 jours (2 + ce jour là )

		#gestion attaque
		if 'attaque' in liste_objet_prit_expedition :
			print()
			liste_objet_prit_expedition.remove('attaque')
			perso_attaque = est_attaque(choix_personne, dico_vie_personnes, liste_objet_prit_expedition, liste_duree_vie_expedition)
			liste_objet_prit_expedition = perso_attaque[0]
			liste_duree_vie_expedition = perso_attaque[1]

		#duree de vie des objets
		if not masque_a_gaz_en_vie(liste_duree_vie_expedition) :
			print()
			print("tu as utilisé le masque à gaz 3 fois")
			print("il ne protège plus correctement et devient inutilisable")
			liste_objet_prit_expedition.remove('masque à gaz')
			while 'masque à gaz' in liste_duree_vie_expedition :
				liste_duree_vie_expedition.remove('masque à gaz') #on retire tous les masque à gaz, si on en retrouve un, on pourra l'utiliser encre 3 fois

		if not fusil_en_vie(liste_duree_vie_expedition) :
			print()
			print("tu as utilisé le fusil 5 fois")
			print("tu n'as plus de balle et il devient donc inutilisable")
			liste_objet_prit_expedition.remove('fusil')
			while 'fusil' in liste_duree_vie_expedition :
				liste_duree_vie_expedition.remove('fusil') #on retire tous 'fusil', si on en retrouve un, on pourra l'utiliser encre 5 fois


		#affichage
		if dico_vie_personnes[choix_personne] > 0 and not('vol' in liste_objet_prit_expedition) :
		#si tjrs envie est pas fait volé (pour pas afficher "rien trouvé" et juste "s'est fait volé")
			print()
			if len(liste_objet_prit_expedition) == 0 :
				if choix_personne == 'fille' or choix_personne == 'femme' :
					print("ta", choix_personne, "n'a rien trouvé lors de son expédition", end='')
				else :
					print("ton", choix_personne, "n'a rien trouvé lors de son expédition", end='')
			else :
				if choix_personne == 'fille' or choix_personne == 'femme' :
					print("ta", choix_personne, "a ramené : ", end='')
				else :
					print("ton", choix_personne, "a ramené : ", end='')
				for i in range(len(liste_objet_prit_expedition)) :
					if i == len(liste_objet_prit_expedition) -1 :
						print(liste_objet_prit_expedition[i], end='')
					else :
						print(liste_objet_prit_expedition[i], end=', ')
			print()
			print()

		#gestion vole
		if 'vol' in liste_objet_prit_expedition :
			print()
			liste_objet_prit_expedition.remove('vol')
			liste_objet_prit_expedition = est_vole(choix_personne, liste_objet_prit_expedition)
			print()

		liste_objet_prit_abri += liste_objet_prit_expedition
		print()
		print("tu as dans ton abri : ",end='')
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





def est_malade(nom_perso, dico_vie_personnes) :
	'''
	Si la personne malade, elle perd 2 fois plus de vie pendant 3 jours et ne
	peut plus partir en expédition

	:param nom_perso: le nom de la personne malade
	:type nom_perso: str
	:param dico_vie_personnes: la vie des personnes
	:type dico_vie_personnes: dict
	'''
	if nom_perso == 'fille' or nom_perso == 'fils' :
		dico_vie_personnes[nom_perso] -= perte_journaliere_vie_enfant #un gosse = plus fragile = perd plus de vie
	else :
		dico_vie_personnes[nom_perso] -= perte_journaliere_vie_parent



def affichage_malade(nom_perso, dico_vie_personnes) :
	'''
	Gère l'affichage des personnes qui sont malades

	:param nom_perso: le nom de la personne malade
	:type nom_perso: str
	:param dico_vie_personnes: la vie des personnes
	:type dico_vie_personnes: dict
	'''
	if nom_perso == 'fille' or nom_perso == 'femme' :
		print("ta", nom_perso, "est tombée malade lors de l'expédition ! ")
	else :
		print("ton", nom_perso, "est tombé malade lors de l'expédition ! ")




def est_attaque(nom_perso, dico_vie_personnes, liste_objet_prit_expedition, liste_duree_vie_expedition) :
	'''
	Gère si la personne se fait attaquer (perd 50PV ou moins si elle a un fusil
	et si elle meurt, elle ne rapporte rien)

	:param nom_perso: le nom de la personne malade
	:type nom_perso: str
	:param dico_vie_personnes: la vie des personnes
	:type dico_vie_personnes: dict
	:param liste_objet_prit_expedition: la liste des objets que la peronne a
	prit lors de l'expédition
	:type liste_objet_prit_expedition: list
	:param liste_duree_vie_expedition: la durée de vie des objets utilisable
	:type liste_duree_vie_expedition: list
	:return: la liste des objet prit lors de l'expédition, et la durée de vie
	des objets utilisables lors des expéditions
	:rtype: tuple (de deux listes)
	'''
	if nom_perso == 'fille' or nom_perso == 'femme' :
		print("ta", nom_perso, "s'est faite attaquée lors de l'expédition ! ")
	else :
		print("ton", nom_perso, "s'est fait attaqué lors de l'expédition ! ")

	if not 'fusil' in liste_objet_prit_expedition : #si perso attaqué et pas de fusil, il perd 50PV
		dico_vie_personnes[nom_perso] -= 50
	elif 'fusil' in liste_objet_prit_expedition : #si perso a un fusil, il peut se defendre
		#affichage
		if nom_perso == 'fille' or nom_perso == 'femme' :
			print("mais elle avait un fusil..")
		else :
			print("mais il avait un fusil..")
		sauvergarde_vie = dico_vie_personnes[nom_perso] #pour dire au joueur si le perso s'est fait tiré dessus ou pas
		nb_assaillants = random.randint(2,3) #entre 2 et 3 assaillants
		for i in range(nb_assaillants) :
			if fusil_en_vie(liste_duree_vie_expedition) :
				liste_duree_vie_expedition.append('fusil') #s'il a des balles, il tire
			else :
				dico_vie_personnes[nom_perso] -= 15 #sinon, il se fait touché mais perd moins de vie que s'il n'avait pas de fusil du tout
		if sauvergarde_vie == dico_vie_personnes[nom_perso] : #si tue tout le monde
			#affichage
			if nom_perso == 'fille' or nom_perso == 'femme' :
				print("et elle a réussie à se défendre")
			else :
				print("et il a réussit à se défendre")

		elif sauvergarde_vie != dico_vie_personnes[nom_perso] : #si pas assez de balle
			#affichage
			if nom_perso == 'fille' or nom_perso =='femme' :
				print("et elle s'est quand même fait touchée ! ")
				print("elle n'avait pas assez de balle !")
			else :
				print("et il s'est quand même fait touché ! ")
				print("il n'avait pas assez de balle !")

	if dico_vie_personnes[nom_perso] <= 0 : #s'il est mort du à l'ataque
		liste_objet_prit_expedition = [] #il ne rapporte rien
		print()
		if nom_perso == 'fille' or nom_perso == 'femme' :
			print("ta", nom_perso, "est morte à cause de son attaque ! ")
		else :
			print("ton", nom_perso, "est mort à cause de son attaque ! ")
	return liste_objet_prit_expedition, liste_duree_vie_expedition




def est_vole(nom_perso, liste_objet_prit_expedition):
	'''
	Si la persone est volée, elle repart sans rien

	:param nom_perso: le nom de la personne volée
	:type nom_perso: str
	:param liste_objet_prit_expedition: la liste des objets que la peronne a
	prit lors de l'expédition
	:type liste_objet_prit_expedition: list
	:return: la liste des objet prit lors de l'expédition
	:rtype: list
	'''
	if nom_perso == 'fille' or nom_perso == 'femme' :
		print("ta", nom_perso, "s'est faite volée lors de l'expédition ! ")
	else :
		print("ton", nom_perso, "s'est fait volé lors de l'expédition ! ")
	liste_objet_prit_expedition = []
	return liste_objet_prit_expedition





def masque_a_gaz_en_vie(liste_duree_vie_expedition):
	'''
	Renvoie True si le masque à gaz est encore utilisable, False sinon

	:param liste_duree_vie_expedition: la liste de durée de vie de tous les
	objets utilisables en expédition
	:type liste_duree_vie_expedition: list
	:return: True ou False
	:rtype: bool
	'''
	compteur = 0
	copie = list(liste_duree_vie_expedition)
	while 'masque à gaz' in copie :
		compteur += 1
		copie.remove('masque à gaz')
	return compteur != 3




def fusil_en_vie(liste_duree_vie_expedition):
	'''
	Renvoie True si le fusil est encore utilisable, False sinon

	:param liste_duree_vie_expedition: la liste de durée de vie de tous les
	objets utilisables en expédition
	:type liste_duree_vie_expedition: list
	:return: True ou False
	:rtype: bool
	'''
	compteur = 0
	copie = list(liste_duree_vie_expedition)
	while 'fusil' in copie :
		compteur += 1
		copie.remove('fusil')
	return compteur != 5