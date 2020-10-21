# Importation de la bibliothèque graphique
import tkinter as tk

# Initialisation du compteur de clics à zéro
compteur = 0
fenetre = None

# Définition de la fonction qui incrémente le compteur de 1
# Elle déclenche un bip sonore si le compteur est supérieur à 10

def incrementer ():
	global compteur #Cette instruction permet d’accéder dans la fonction à la variable compteur définie en dehors de la fonction
	global fenetre
	compteur = compteur + 1
	if compteur >= 10:
		fenetre.bell()
	return compteur

# Définition de la fonction qui met à jour l’affichage de la valeur du compteur dans l’IHM 
def action_clic():
	
	# Création de la fenêtre de l’IHM
	global fenetre
	if not fenetre :
		fenetre = tk.Tk() 
	# Affectation d’un titre à la fenêtre
	fenetre.title("Compter les clics") 
	# Dimensionnement et positionnement de la fenêtre
	fenetre.geometry("300x125+400+400") 
	# Création de la zone de texte pour l’explication
	labelExpl = tk.Label(fenetre, text="Je compte le nombre de clics sur le bouton")
	# Création de la zone de texte pour l'intitulé devant le compteur
	labelCompteur1 = tk.Label(fenetre, text="Nombre de clics: ") 
	# Création de la zone de texte pour l’affichage du compteur
	labelCompteur2 = tk.Label(fenetre, text="0") 
	# Positionnement de la zone du texte explicatif et dimensionnement de ses marges 
	labelExpl.grid(row=0, column=0, columnspan=3, padx = 5, pady = 5)
	# Positionnement de la zone du texte de l’intitulé et dimensionnement de ses marges 
	labelCompteur1.grid(row=1, column=1, padx = 5, pady = 5)
	# Positionnement de la zone du texte du compteur et dimensionnement de ses marges 
	labelCompteur2.grid(row=1, column=2, padx = 5, pady = 5)
	labelCompteur2.config(text=str(incrementer()))
	# Création du bouton associé au compteur
	bouton = tk.Button(fenetre, text="Cliquez-moi !", command = action_clic) 
	# Positionnement du bouton associé au compteur et dimensionnement de ses marges 
	bouton.grid(row=1, column=0, padx = 5, pady = 5)
	# Création du bouton quitter
	BoutonQuitter = tk.Button(fenetre, text ="Quitter", command = fenetre.destroy)
	# Positionnement du bouton quitter et dimensionnement de ses marges
	BoutonQuitter.grid(row=2, column=0, columnspan=3, padx = 5, pady = 5)
	# Écoute en permanence des évènements sur les périphériques d’entrée pour pouvoir capter le clic gauche de la souris
	fenetre.mainloop()


if __name__ == '__main__':
	action_clic()


