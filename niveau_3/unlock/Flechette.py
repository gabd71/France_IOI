""" Ne pas copier se code, il est ici pour être amélioré par la communauté """

#TODO à commenter


#Récuperation des données du problemes
lon = int(input())

#Coeur du programme
def cible(n):
    taille = 2*n-1  #Taille de la cible en fonction du nombre de de lettre
    cible_base = [[None for i in range(taille)] for f in range(taille)]
    lettre = "abcdefghijklmnopqrstuvwxyz"
    l=0
    for ligne in range(len(cible_base)):
        for i in range(l,len(cible_base[ligne])-l):
            cible_base[ligne][i] = lettre[l]
            cible_base[-ligne+taille-1][i] = lettre[l]
            cible_base[i][ligne] = lettre[l]
            cible_base[i][-ligne+taille-1] = lettre[l]
        l +=1
    for i in range(len(cible_base)):
       cible_base[i] = "".join(cible_base[i])
    cible_base = "\n".join(cible_base)
    return cible_base
    
    
print(cible(lon))
