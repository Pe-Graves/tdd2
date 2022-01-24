def miroir(mot,indice):
    res = ""
    if mot == "" or mot == " " or type(mot) != str or len(mot) <= indice:
        return ""
    for i in range(indice,-1,-1):
        res = res + mot[i]
    return mot[:indice+1] + res
