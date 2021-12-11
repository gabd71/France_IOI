""" Ne pas copier se code, il est ici pour être amélioré par la communauté """

#TODO à commenter


# récuperation des variables
recup = input().split(" ")
nbLivres = int(recup[0])
nbJours = int(recup[1])
reserve = []
for i in range(int(nbLivres)):
   reserve.append(0)



# coeur du programme
for i in range(nbJours):
    nb = int(input())
    for p in range(nb):
        l3 = input().split(" ")
        livre = int(l3[0])
        temps = int(l3[1])
        if reserve[livre]<=0:
            reserve[livre] = temps
            print(1)
        else:
            print(0)
    for j in range(len(reserve)):
        reserve[j] -= 1
    
