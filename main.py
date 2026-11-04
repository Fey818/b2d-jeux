#initialiser la db
#message de bienvenue
#demander un choix entre (1 lancer une partie ,2 Tableau des score,3 quittez)

#verifier le choix 
    #Boucle infini
        #choix (minimum,maximum)
        #si le min <= choix <= max
            #interompre le code
        #sinon
            #réessayer

#si l'ultilisateur choisi 1

#demander un nom d'utilisateur
    #delander de taper un nom
    #verifier si le nom est correct
    #retourner le nom correct

#verifier si le nom est correct
    #si le nom contient des caracetre hors alphabet
        #interompre le code
    #autre 
        #réessayer


#demander de cree une equipe
    #cree une liste vide
    #afficher tout les perso disponible
    #demander de choisir 3 perso
    #retourner les perso chosis

#afficher personnage dispo
    #pour nom et stats dans la liste des personnage
    #afficher les perssonage

#demander de choisir 3 perso
    #tant que equipe n'est pas < 3
        #demander d'ecrire les numero de perssonage voulue
            #si perso deja dans equipe 
                #deja seelectionner 
            #autre perso pas dans perssonage
                #pas danss la liste

#lancer le round
    #lancer la boucle des round

#lancer la boucle des round
    #tant que 1 des perssonage est en vie
        #lancer un choix au hasard d'un monstre
        #tour des attaquant 
    
#lancer un choix au hasard d'un monstre
    #Pour nom et stat dans la liste des montstre
        #lancer un choix aleatoire 
        #retourner son nom et ses stats

#tour des attaquant
    #calculer les degats cause par l'equipee
    #retrourner la vie du monstre
    ##verifier quelle personnage sont encore en vie

#tour du monstre
    #verifier hp







#initialiser la db
#Bienvenue dans le jeu
#choisir un mode de jeu
    #1 lancer une partie,2 Tableau des score,3 Quittez

#verifier l'input TODO:
    #tant que vraie
        #choix = int (min,max)
            #si min <= choix <= max
            #break
            #sinon 
            #veuillez reesaier  
        #return choix

#lancer le menu 
    #choisir mode de jeu
    #verifier l'input

#a choisis lancer une partie

#mettre nom TODO:
#cree equipe
#round

#enregistre score dans la db
    #rammener vers le menu du debut



#mettre nom 
    #nom = input"Mettez votre nom"
    #verifier nom correct
    #return nom

#verifier nom corect
    #if nom .isalpha()
    #break
    #else 
    #veuillez retapez



#recuperer l'equipe
        #tant que equipe n'est pas < 3
            #taper les numero des perssonage
            #si perso deja dans equipe 
                #deja seelectionner 
            #autre perso pas dans perssonage
                #pas danss la liste


#afficher perso
    #pour nom, stats dans perso
    #afficher perso


#cree equipe
    #equipe = []
    #afficher perso
    #chosir sa team de 3
        #recuperer l'equipe
    #return equipe



#round 
    #recuperer l'equipe
    #tant que hp hero > 0
        #choix monstre au hasard
        #lancer round
        



#lancer round
    #tant que hp monstre > 0
        #tour hero
        #verifier hp monstre
        #tour monstre
    #return hp hero

#choix monstre random
    #nom,stat = random.choice(list(monstre))
    #"Monstre choisis aleatoirement"
    #return nom,stats

#verifier hp hero
    #si perso <= 0
        #rendre inactif le perso 
        #montrer perso actif
    #retourner les hp    

#rendre inactif le perso 
    #perso[].is_active = false

#montrer persso actif
    #actif = [obj for obj in perso if obj.is_active]
    


#tour hero
    #attaquer equipe
    #verifier hp_monstre

#attaque equipe
    #pour nom dans equipe
        #attaque = perssonage [nom]["Attack"]
        #defense = monstre [1]["Defense"]
        #degats = attaque - (defense // 2)
        #hp_monstre = hp_monstre - degats




#tour monstre
    #verifier hp_monstre

    #verifier hp hero     


#verifier hp_monstre 
    #si hp_monstre <= 0
        #mort
    #else 
        #return hp_monstre




#a choisis score TODO:
#montrer tout less score enregistre depuis la db
#montre top 3


#a chosis de quittez le jeu  TODO:
#quit













                            #verifier hp_monstre
                                #hp_monstre = monstre [1]["HP"]

#recup hp hero
    #hp_equipe = perssonage [1]["HP"]





#verifier hp_monstre 
    #si hp_monstre <= 0
        #mort
    #else 
        #return hp_monstre









#verifier equipe vivante
    #tant que perssonage > 0 
            #montrer l'equipe restante
            #refaire un tour
    #return score