#initialiser la db
#Bienvenue dans le jeu
#choisir un mode de jeu
    #1 lancer une partie,2 Tableau des score,3 Quittez

#verifier l'input
    #tant que vr
        #que le int(min,max)
    #exept
        #mauvais nombre ressaier
    #return int

#lancer le menu 
    #choisir mode de jeu
    #verifier l'input

#a choisis lancer une partie

#mettre nom

#cree equipe

#choix monstre random

#tour hero 


#tour monstre 

#verifier equipe vivante
    
#enregistre score dans la db
    #rammener vers le menu du debut



#mettre nom 
    #nom = input"Mettez votre nom"
    #verifier nom correct
    #return nom
#nom 
    #mettre nom
    #return nom
#verifier nom 



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



#choix monstre random
    #nom,stat = random.choice(list(monstre))
    #"Monstre choisis aleatoirement"
    #return nom,stats


                            #verifier hp_monstre
                                #hp_monstre = monstre [1]["HP"]

#recup hp hero
    #hp_equipe = perssonage [1]["HP"]



#attaque equipe
    #pour nom dans equipe
        #attaque = perssonage [nom]["Attack"]
        #defense = monstre [1]["Defense"]
        #degats = attaque - (defense // 3)

        #hp_monstre = hp_monstre - degats


#verifier hp_monstre 
    #si hp_monstre <= 0
        #mort
    #else 
        #return hp_monstre



#verifier perso mort
 #si perso <= 0
            #rendre inactif le perso 
        #retourner les hp    



#tour hero
    #attaquer equipe
    #verifier hp_monstre




#tour monstre
    #verifier hp_monstre

    #verifier perso mort      

#verifier equipe viavnte
    #tant que perssonage > 0 
            #montrer l'equipe restante
            #refaire un tour


#a choisis score
#montrer tout less score enregistre depuis la db

#a chosis de quittez le jeu

 