def fonction1(x):
    return 5*x**2

def fonction2(x):
    return 3*x

def fonction3(x):
    return 1/x


def approximation(fonction, ordre, point):

    if ordre > 0 and ordre < 1 and point != 0:
        res = fonction(point)
        multi_ordre = 1 / ordre
        res *= multi_ordre
        res = int(res)
        return res*ordre
    
    if ordre >= 1 and point != 0:
        return fonction(point)

    if ordre <= 0 or point == 0:
        return 0
