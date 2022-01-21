def deriveeSeconde(floatListe):
    tab = []
    res = []
    temp = 2 # interval de temps régulier
    for i in floatListe:
        if type(i) != float:
            return [0.0]
    if(floatListe == [] or len(floatListe) < 3):
        return [0.0]
    for i in range(len(floatListe)-1):
        tab.append((floatListe[i+1]-floatListe[i])/temp)
    if(tab == [] or len(tab) < 2):
        return [0.0]
    for j in range(len(tab)-1):
        res.append((tab[j+1]-tab[j])/temp)
    return res

