def fonction1(x):
    return 5*x**2

def fonction2(x):
    return 3*x

def fonction3(x):
    if x == 0:
        return 0
    return 1/x


def approximation(fonction, ordre, point):

    if type(ordre) != float or type(point) != float or ordre <= 0.0:
        return 0

    if ordre >= 1.0:
        return fonction(point)
    
    ordre_inverse = 1.0/ordre
    verif_ordre = ordre*ordre_inverse

    if ordre_inverse%10 != 0:
        return 0

    if ordre > 0.0 and ordre < 1.0:
        res = fonction(point)
        multi_ordre = 1/ordre
        res *= multi_ordre
        res = int(res)
        return res*ordre
    
    

    
