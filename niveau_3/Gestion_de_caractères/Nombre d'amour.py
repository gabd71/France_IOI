""" Ne pas copier se code, il est ici pour être amélioré par la communauté """

#TODO à commenter


# récuperation des variables

def amour(nom):
    res = 0
    for i in nom:
        res += ord(i)-65
    while res >= 10:
        res2 = 0
        for i in str(res):
            res2 += int(i)
        res = res2
    return res
    
rep = [str(amour(i)) for i in input().split(" ")]
print(" ".join(rep))
