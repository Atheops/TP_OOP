releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(releve1):
    releve = "Capteur "+releve1[0] + " : " + str(releve1[1])+" "+releve1[2]
    return releve 
   
print(afficher_releve(releve1))


assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"


def recalibrer(releves, typecapteur, newvalue):
    newlist=[]
    for releve in releves :
        if typecapteur == releve[0]:
            nouveau_releve = (releve[0], newvalue ,releve[2])
            newlist.append(nouveau_releve)
        else :
            newlist.append(releve)

    return newlist

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
print (nouveaux_releves)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3