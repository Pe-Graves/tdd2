def derivee(floatListe):
    tab = []
    temp = 2 # interval de temps régulier
    for i in floatListe:
        if type(i) != float:
            return [0.0]
    if(floatListe == [] or len(floatListe) < 2):
        return [0.0]
    for i in range(len(floatListe)-1):
        tab.append((floatListe[i+1]-floatListe[i])/temp)
    return tab

