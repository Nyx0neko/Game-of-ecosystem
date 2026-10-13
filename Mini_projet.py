# Importation de la fonction aléatoire
from random import uniform

# Création des variables de départ 
plantes = 20000000000
herbivores = 400
carnivores = 20

# Création des variable de taux de reproduction 
repro_plantes = 0.20
repro_herbivores = 0.10
repro_carnivores = 0.05

# Creation de variable de besoin
besoin_herbivores = 10
besoin_carnivore = 5

# Demande a l'utilisateur le nombre de tours qu'il souhaite
nbr_tour = int(input("Entrer le nombre de tour : "))

# Informe l'utilisateur de la situation de départ
print("Situation initiale : \nLe nombre de plantes est : " + str(plantes) + 
      "\nLe nombre d'herbivores est : " + str(herbivores) +
      "\nLe nombre de carnivores est : " + str(carnivores) +
      "\nOn joue pour : " + str(nbr_tour) + " tours")

# Création d'une boucle qui tournera pour le nombre de tours set par l'utilisateur
for tour in range(1,nbr_tour+1) :
    # Affichage du tour actuel
    print("--- Tour " + str(tour) + " ---")

    # 1 reproduction des plantes, prends une valeur aléatoire entre 0 et le taux de reproduction des plantes
    plantes += int(plantes * uniform(0, repro_plantes))

    # 2. Nutrition et reproduction des herbivores
    # Calcule de la consomation des plantes
    plantes_conso = herbivores * besoin_herbivores
    # Condition : si on a moins de consommation que de plante
    if plantes_conso <= plantes:
        # Soustraction de la consomation au nombre de plante
        plantes -= plantes_conso
        # Reproduction des herbivores
        herbivores += int(herbivores * repro_herbivores)
    # Si on a plus de consommation de plantes que de plantes
    else:
        # Set du nombre dherbivore a ceux qui on pu être nourit
        herbivores = plantes // besoin_herbivores
        # Set des plantes à 0
        plantes = 0

    # 3 Nutrition et reproduction des carnivores
    # 3.1 Calcule le nombre d'herbivores qui vont être consommés
    herbivores_conso = carnivores * besoin_carnivore
    # 3.2 Condition qui calcule si il y a suffisement d'herbivore pour nourir les carnivores
    if herbivores_conso <= herbivores :
        # Soustraction des herbivores consommés aux herbivores
        herbivores -= herbivores_conso
        # Calcule le taux de reproduction des herbivores
        carnivores += int(carnivores * repro_carnivores)
    else : 
        # Sinon on retire le nombre de carnivore qui meurt en ne gardant que ceux que on peut nourir
        carnivores = herbivores // besoin_carnivore
        # On set la variable herbivore a 0
        herbivores = 0

    # Affiche le nombre de plantes, herbivores et carnivore restant ainsi que le tours actuelle
    print("Le nombre de plantes est de " + str(plantes) + ", celui de herbivores est de " + str(herbivores) + ", et celui de carnivores est de " + str(carnivores) + " au tour " + str(tour))
    # Fin du jeu si une espèce disparait
    if plantes == 0 or herbivores == 0 or carnivores == 0 :
        print("Le jeu c'est terminer avec : " + str(tour))
        break
    

