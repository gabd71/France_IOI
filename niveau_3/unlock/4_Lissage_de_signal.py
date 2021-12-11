
""" Ne pas copier se code, il est ici pour être amélioré par la communauté """

#TODO à commenter
#TODO changer boucle while


# récuperation des variables

n = int(input())
dif = float(input())
l = []
for i in range(n):
   l.append(float(input()))

    
#coeur du programme
def lissage(diffMax,l):
    n = 0
    while 1:
        nb_check = 0
        for i in range(0,len(l)-1):
            if abs(l[i]-l[i+1])>=diffMax:
                nb_check+= 1
        if nb_check == 0:
            return(n)

        l_save = l[:]
        for i in range(1,len(l)-1):
            l[i]= (l_save[i-1]+l_save[i+1])/2
        n+= 1

        
print(lissage(dif,l))
