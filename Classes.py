import random
import numpy as np
### Penser que pendant les manches il y a la couleur demandée et l'atout

################
''' 
peut être plutôt faire en sorte qu'il y ait au départ la création de 4 joueurs stochés dans  équipes
partie ne prend en argument que les équipes

- s'ocupper de la fonction attribution_points des cartes
- faire suite la méthode déterminer le gagnant de la manche
- méthode dans équipes pour connaitre le nb de point possédé

- méthode dans manche jouer_manche = play des 4 joueurs

- méthode pour jouer des joeurs la séparer en 3 fonctions 1 Islegal / 1 boucle / 1 de choix (=random actuellement)
- méthode pour dire si équipe qui prend à gagné 

'''


class Carte:
    liste_carte = []
    Dic_valeur = {'7': "7", '8': "8", '9': "9", '10': "10",
                  '11': "V", '12': "D", '13': "R", '14': "A"}
    Dic_couleur = {'0': "pique", '1': "coeur", '2': "carreau", '3': "trefle"}
    Dic_point = {'7': "0", '8': "0", '9': "0", '10': "10",
                 'V': "2", 'D': "0", 'R': "4", 'A': "11", '9A': "14", 'VA': "20"}

    # couleur = ""
    # valeur =""
    # point = 0

    def __init__(self, valeur,couleur):
        self.valeur = valeur
        self.couleur = couleur
        self.points = 0

    def __str__(self):
        return f" {self.valeur} {self.couleur} "

    def attributer_point(self, atout):
        '''utiliser les dictionnaires situées dans PaquetsDeCartes pour attribuer les vraies point'''
        if self.couleur != atout:
            self.points = int(self.Dic_point[self.valeur])
        else:
            if self.valeur == 'V':
                self.points = 20
            if self.valeur == "9":
                self.points = 14

class Equipe:
    # points = 0
    # plis = []
    # nom = []

    def __init__(self,nom, joueur1, joueur2):
        self.nom = nom
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.tas = []
        self.points_equipe = 0

    def actualiser_point(self):
        inter = 0
        for c in self.tas:
            inter += c.points
        self.points_equipe = inter

class Joueur:
    '''
    peut être ajouter un attribut jouable qui s'actualise à chaqye fois ce qui permettra à l'IA de faire ses choix toute
        en respectant les règles '''
    main =[]
    nom = []


    def __init__(self,nom):
        self.nom = nom
        self.meneur = ""

    def __str__(self):
        resultat = ""
        for carte in self.main:
            resultat += str(carte)
        return resultat

    def jouer(self,manche):
        #a refaire en prenant en comtpe les notes
        if len(manche.table) ==0:
            #pas encore de carte sur la table -> premier joueur joue ce qu'il veut
            carte_id = np.random.randint(0,len(self.main))
            carte = self.main[carte_id]
            manche.append(carte)
        else:
            # pique, coeur, carreau, trefle = 0, 0, 0, 0
            # for c in self.main:
            #     if c.couleur == "pique":
            #         pique = 1
            #     if c.couleur == "coeur":
            #         coeur = 1
            #     if c.couleur == "carreau":
            #         carreau = 1
            #     if c.couleur == "trefle":
            #         trefle = 1
            #il possède la couleur et doit donc jouer de force
            demande = manche.table[0].couleur
            jouable = []
            for c in self.main:
                if c.couleur == demande:
                    jouable.append(c)
            if len(jouable) != 0:
                carte_id = np.random.randint(0,len(self.main))
                carte = jouable[carte_id]
                manche.append(carte)
            else:
                #défausse
                carte_id = np.random.randint(0, len(self.main))
                carte = jouable[carte_id]
                manche.append(carte)

    def trouver_equipe(self,Partie):
        '''méthode pour trouver l'équipe d'un joueur sans modifier trop le code
        renvoie l'équipe de joueur'''
        for l in Partie.liste_equipe:
            if self in l:
                return l

class PaquetDeCarte:
    '''
    Quand on crée un paquet, il est automatiquement remplie de toutes les cartes
    '''
    liste_carte =[]
    Dic_valeur = {'7': "7", '8': "8", '9': "9", '10': "10",
                  '11': "V", '12': "D", '13': "R", '14': "A"}
    Dic_couleur ={'0': "pique", '1': "coeur", '2':"carreau", '3':"trefle"}
    Dic_point = {'7': "0", '8': "0", '9': "0", '10': "10",
                  'V': "2", 'D': "0", 'R': "4", 'A': "11", '9A':"14", 'VA':"20"}
    def __init__(self):
        for i in range(4):
            for j in range(7,15):
                carte = Carte(self.Dic_valeur[str(j)],self.Dic_couleur[str(i)])
                self.liste_carte.append(carte)

    def __str__(self):
        resultat = ""
        for i in range(4):
            for carte in self.liste_carte[i * 8: (i + 1) * 8]:
                resultat += str(carte) + " "
            resultat += "\n"
        return resultat

    def melanger(self):
        random.shuffle(self.liste_carte)

class Partie:
    # joueur1 = Joueur
    # joueur2 = Joueur
    # joueur3 = Joueur
    # joueur4 = Joueur
    # deck = PaquetDeCarte

    def __init__(self,equipe1,equipe2):
        self.liste_equipe = [equipe1, equipe2]
        self.joueur1 = equipe1.joueur1
        self.joueur2 = equipe1.joueur2
        self.joueur3 = equipe2.joueur1
        self.joueur4 = equipe2.joueur2
        self.liste_joueur = [self.joueur1,self.joueur2,self.joueur3, self.joueur4 ]
        self.deck = PaquetDeCarte
        self.meneur =""
        self.atout = ""
        self.tour = 0
        self.historique = ""

    def distrib(self):
        self.deck.melanger()
        for i in range(8):
            self.joueur1.main.append(self.deck.liste_carte.pop())
            self.joueur2.main.append(self.deck.liste_carte.pop())
            self.joueur3.main.append(self.deck.liste_carte.pop())
            self.joueur4.main.append(self.deck.liste_carte.pop())


    #choix du meneur et de l'atout aléatoirement pour dvp et tester les
    # les autres méthodes développées

    def choix_atout(self):
        atout_id = np.random.randint(0,len(self.deck.liste_carte))
        self.atout = self.deck.liste_carte[atout_id]
        print("atout choisi :" + str(self.atout))

    def choix_meneur(self):
        meneur_id = np.random.randint(0, len(self.liste_joueur))
        self.meneur = self.liste_joueur[meneur_id]
        print ("meneur choisi :" + str(self.meneur))

    #attribution des valeurs des cartes après que l'atout est était choisi
    def valeur_carte(self):
        for c in self.deck.liste_carte:
            c.attributer_point(self.atout)
            print("valeur des cartes actualisées")

    def show_historique(self):
        i = 0
        for m in self.historique:
            i += 1
            print("manche numéro" + str(i))
            print(m)




class Manche:
    '''
    coder les règles pour décider qui va remporter le pli
    '''

    def __init__(self, partie):
        self.partie = partie
        self.meneur = partie.meneur
        self.atout = partie.atout
        self.table =[] #carte actuellement sur la table

    # def play(self,joueur):
    #     pique, coeur, carreau, trefle = 0, 0, 0, 0
    #     for c in joueur.main:
    #         if c.couleur == "pique":
    #             pique = 1
    #         if c.couleur == "coeur":
    #             coeur = 1
    #         if c.couleur == "carreau":
    #             carreau = 1
    #         if c.couleur == "trefle":
    #             trefle = 1
    #
    #
    #
    #     carte = joueur.main
    #
    # def jouable(self,joueur):


    # def isvalid(self, carte, joueur):
    #     #meme couleur
    #     if carte.couleur == self.table[-1]:
    #         return True
    #     else:
    #         for c in joueur.main
    #
    #     pass

    def gagnant_manche(self):
        liste_gagnant = []
        for c in self.table:
            #cas atout
            if c.couleur == self.atout:
                liste_gagnant.append(c)
                gagnant = liste_gagnant[0]
                for c in liste_gagnant:
                    if c.point > gagnant.point:
                        gagnant = c

            # cas sans atout
            if c.couleur == self.table[0].couleur:
                liste_gagnant.append(c)
                gagnant = liste_gagnant[0]
                for c in liste_gagnant:
                    if c.point > gagnant.point:
                        gagnant = c
        # trouver à qui appartient la carte gagnante et lui donner la main pour la prochaine manche
        gagnant_index_relatif = self.table.index(c)
        meneur_index = self.partie.liste_joueur.index(self.meneur)
        gagnant_index = (gagnant_index_relatif + meneur_index) % 4
        self.partie.historique.append(self.table)
        print("gagnant est le joueur numéro :" + str(gagnant_index))
        #gagnat trouvé attribution des résultats
        joueur_gagnant = self.partie.liste_joueur[gagnant_index]
        self.partie.meneur = joueur_gagnant
        equipe_gagnante = joueur_gagnant.trouver_equipe()

        #ajout des cartes 1 à 1 pour ne pas avoir une liste de liste de cartes
        for c in self.table:
            equipe_gagnante.tas.append(c)
        equipe_gagnante.actualiser_point()

    def jouer_manche(self):
        for p in self.partie.liste_joueur:
            p.jouer


    def __str__(self):
        return f"carte jouées {self.table[0]}, {self.table[1]}, {self.table[2]}, {self.table[3]}"
