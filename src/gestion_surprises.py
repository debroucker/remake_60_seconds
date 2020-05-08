# -*- coding: utf-8 -*-
import random
import time

def surprise(liste_objet_prit_abri):
	'''
	Une personne frappe à l'abi, soit elle est veut te donner un objet,t'en
	demandé un, t'en voler un ou de te proposer un échange (pas obligé d'ouvrir)

	:param liste_objet_prit_abri: la liste des objets prit dans l'abri
	:type liste_objet_prit_abri: list
	'''
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
	liste_surprise = ['bienveillant','echange', 'pillard', 'aide']
	random.shuffle(liste_surprise)
	print("on frappe à la porte de ton abri...")
	print()
	print("veux-tu ouvrir ?")
	choix = input("'oui' ou 'non' : ")
	#assert
	while choix not in ['oui', 'non']:
		print("SAISIR 'oui' OU 'non' !")
		choix = input("'oui' ou 'non' : ")
	if choix == 'oui' :
		print()
		hasard = liste_surprise[0]
		if hasard == 'bienveillant' :
			inconnu_bienveillant(liste_objet_prit_abri)
		elif hasard == 'echange' :
			inconnu_echange(liste_objet_prit_abri)
		elif hasard == 'pillard' :
			inconnu_pillard(liste_objet_prit_abri)
		elif hasard == 'aide' :
			inconnu_aide(liste_objet_prit_abri, liste_surprise)





def inconnu_bienveillant(liste_objet_prit_abri) :
	'''
	La personne qui frappe à l'arbi est bienveillante : elle donne un objet

	:param liste_objet_prit_abri: la liste des objets prit dans l'abri
	:type liste_objet_prit_abri: list
	'''
	print("c'est une personne qui passait dans le coin")
	print("elle a prit trop d'objet sur elle et propose de t'en donner un")
	liste_objet_inconnu = ['eau', 'bouffe', 'sac', 'fusil', 'four', 'cachets', 'masque à gaz']
	random.shuffle(liste_objet_inconnu)
	objet_inconnu = liste_objet_inconnu[0]
	print("elle t'a donné :", objet_inconnu)
	liste_objet_prit_abri.append(objet_inconnu)




def inconnu_echange(liste_objet_prit_abri) :
	'''
	La personne qui frappe à l'arbi propose un échange

	:param liste_objet_prit_abri: la liste des objets prit dans l'abri
	:type liste_objet_prit_abri: list
	'''
	print("c'est une personne qui passait dans le coin")
	print("elle te propose un echange d'objet")
	liste_objet_inconnu = ['eau', 'bouffe', 'sac', 'fusil', 'four', 'cachets', 'masque à gaz']
	random.shuffle(liste_objet_inconnu)
	objet_inconnu = liste_objet_inconnu[0]
	objet_inconnu_echange = liste_objet_inconnu[1]
	print("elle te propose : " + str(objet_inconnu) + "; contre : " + str(objet_inconnu_echange))
	print()
	#si l'echange est possible
	if objet_inconnu in liste_objet_prit_abri :
		print("acceptes-tu l'échange ?")
		choix = input("'oui' ou 'non' : ")
		#assert
		while choix not in ['oui', 'non']:
			print("SAISIR 'oui' OU 'non' !")
			choix = input("'oui' ou 'non' : ")
	elif objet_inconnu not in liste_objet_prit_abri :
		print("tu n'as pas l'objet demandé")
		print("tu ne peux pas procéder à l'échange")
		choix = 'non'
	if choix == 'oui' :
		print("tu as écangé :" + str(objet_inconnu) + "; contre : " + str(objet_inconnu_echange))
		liste_objet_prit_abri.append(objet_inconnu)
		liste_objet_prit_abri.remove(objet_inconnu_echange)




def inconnu_pillard(liste_objet_prit_abri) :
	'''
	La personne qui frappe à l'arbi est un pillard : elle vole un objet s'il
	est dans l'abri, sinon elle vole 5 objets ou tout s'il y a moins de 5 objets

	:param liste_objet_prit_abri: la liste des objets prit dans l'abri
	:type liste_objet_prit_abri: list
	'''
	liste_objet_inconnu = ['eau', 'bouffe', 'sac', 'fusil', 'four', 'cachets', 'masque à gaz']
	random.shuffle(liste_objet_inconnu)
	objet_inconnu = liste_objet_inconnu[0]
	print("c'est une bande de pillard !")
	print("ils réclament :", objet_inconnu)
	print()
	#si le vol est possible
	if objet_inconnu in liste_objet_prit_abri :
		liste_objet_prit_abri.remove(objet_inconnu)
		print("tu as perdu :", objet_inconnu)
	#si pas objet voulu, il perd soit 5 objets, soit tous s'il n'a pas au moins 5 objets
	elif objet_inconnu not in liste_objet_prit_abri :
		random.shuffle(liste_objet_prit_abri)
		print("tu n'as pas l'objet demandé !")
		if len(liste_objet_prit_abri) >= 5 :
			print("ils t'ont volé 5 objets :", end='')
			for i in range(4) :
				print(liste_objet_prit_abri[0], end=', ')
				liste_objet_prit_abri.remove(liste_objet_prit_abri[0])
			print(liste_objet_prit_abri[0], end='')
			liste_objet_prit_abri.remove(liste_objet_prit_abri[0])
			print()
		else : #soit tous s'il n'a pas au moins 5 objets
			print("ils t'ont tout volé !")
			while len(liste_objet_prit_abri) > 0 :
				liste_objet_prit_abri.remove(liste_objet_prit_abri[0])





def inconnu_aide(liste_objet_prit_abri, liste_surprise) :
	'''
	La personne qui frappe à l'abri demande de l'aide
	Si tu aides la personne, tu as plus de chance d'avoir un "bienveillant" ou
	un "echange" qui frappe à la porte
	Si tu décides de ne pas l'aider, tu as plus de chance d'avoir un "pillard"
	qui frappe à la porte


	:param liste_objet_prit_abri: la liste des objets prit dans l'abri
	:type liste_objet_prit_abri: list
	:param liste_surprise: la liste des differentes personnes qui frappe à l'bri
	:type liste_surprise: list
	'''
	liste_objet_inconnu = ['eau', 'bouffe', 'sac', 'fusil', 'four', 'cachets', 'masque à gaz']
	random.shuffle(liste_objet_inconnu)
	objet_inconnu = liste_objet_inconnu[0]
	print("c'est une personne qui passait dans le coin")
	print("elle te demande si tu aurais la gentillese de lui donner :", objet_inconnu)
	print()
	#si l'echange est possible
	if objet_inconnu in liste_objet_prit_abri :
		print("acceptes-tu de l'aider ?")
		choix = input("'oui' ou 'non' : ")
		#assert
		while choix not in ['oui', 'non']:
			print("SAISIR 'oui' OU 'non' !")
			choix = input("'oui' ou 'non' : ")
	elif objet_inconnu not in liste_objet_prit_abri :
		print("tu n'as pas l'objet demandé")
		print("tu ne peux donc pas l'aider")
		choix = 'non_pas_objet'
	if choix == 'oui' :
		print()
		print("tu as donné :", objet_inconnu)
		liste_objet_prit_abri.remove(objet_inconnu)
		#si tu aides la personne, tu as plus de chance d'avoir un bienveillant ou un echange qui frappe à ta porte
		liste_surprise.append('donneur')
		liste_surprise.append('echangeur')
	elif choix == 'non' : #si tu decide de ne pas l'aider (et non que tu peux pas) tu a plus de chance de tomber sur des pilards
		liste_surprise.append('pillard')