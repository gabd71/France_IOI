
""" Ne pas copier se code, il est ici pour être amélioré par la communauté """

#TODO à commenter
#TODO modifier la boucle while

#Récuperation des données du problemes

compo = list(input(""))

save = []
test = 1
a = 0


#Coeur du programme 
while test != 0:
    test = 0
    save = []
    c=1
    while c <= len(compo)-1:
        if len(compo)==1:
            test = 0
        elif compo[c-1] == compo[c]:
            save.append(c-1)
            save.append(c)
            test += 1
            
        a = 0
        for p in save:
            del compo[p+a]
            a-=1
            c+=1
        save = []
        
        c+= 1
print("".join(compo))
