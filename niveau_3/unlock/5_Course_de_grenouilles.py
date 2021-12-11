""" Ne pas copier se code, il est ici pour être amélioré par la communauté """

#TODO à commenter


total=0
nbGrenouilles=int(input())
nbTours=int(input())


def EnTete(liste,nb) :
   nbEnTete=0
   maximum=max(liste)
   for i in range(nb) :
      if liste[i]==maximum :
         nbEnTete+=1
   return nbEnTete


compteEnTete=[0]*(nbGrenouilles)
liste=[0]*(nbGrenouilles)

for i in range(nbTours-1) :
   numGrenouille,distance=map(int,input().split(" "))
   total=liste[numGrenouille-1]+distance
   if total>max(liste) :
      compteEnTete[numGrenouille-1]+=1
   elif total<max(liste) and EnTete(liste,nbGrenouilles)==1 :
      compteEnTete[liste.index(max(liste))]+=1
   liste[numGrenouille-1]+=distance
  
print(compteEnTete.index(max(compteEnTete))+1)
