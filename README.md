# tdd2
Rattrapage - TDD - TD2

Commandes de Github:

- git init
- git status = voir toutes les actions réalisées
- git diff = permet de voir les conflits
- git clone adresse https ou SSH
- git pull
- git branch Nom_De_la_Branche   = créer une nouvelle branche
- git branch -r = permet de voir toutes les branches du github
- git chekcout Nom_De_la_Branche = basculer sur une branche
- git add Nom_Du_Fichier
- git reset = permet d'annuler un git add
- git commit -m "Objet du commit"
- git push


Exercice 1 : Miroir

- Implémentation d'une fonction miroir qui prend en entrée un string et renvoie son miroir à partir d'un entier donné
  C'est-à-dire soit le string azertyuiop, si on prend l'indice 3, la fonction renvoie azerreza

  Dans cette fonction : 
  
  - return un string vide, si on a un string vide en entrée

  - return un string vide, si l'indice >= à la longueur de la chaîne

Exercice 2 : Derivee

- Implémenter une fonction qui prend en paramètre une liste de float et calcule sa dérivée, on considérera que les échantillons sont pris à interval de temps régulier

  Dans cette fonction : 

  - return une liste = [0.0] dans le cas, où le type d'un élément de la liste est différent de float

  - return une liste = [0.0] dans le cas, où le nombre d'éléments de la liste d'entrée est inférieur à 2

  - return une liste = [0.0] dans le cas, où la liste en entrée est vide

  - on prend un interval de temps régulier égal à 2 

Exercice 3 : Derivee Seconde

- Implementer une fonction qui prend en paramètre une liste de float et calcule sa dérivée seconde, on considèrera que les échantillons sont tous pris à interval de temps régulier

  Dans cette fonction :

  - return une liste = [0.0] dans le cas, où le type d'un élément de la liste est différent de float,

  - return une liste = [0.0] dans le cas, où le nombre d'éléments de la liste est inférieur à 3

  - return une liste = [0.0] dans le cas, où la liste en entrée est vide,

  - on prend un interval de temps régulier égal à 2


Exercice 4 : Approximation de la dérivée d'une fonction

- Implémenter une fonction qui prend en paramètre la dérivée d'une fonction, un ordre de grandeur défini ainsi que un point et qui calculera l'approximation de la dérivée de cette fonction en ce point

  Dans cette fonction : 

  - return 0 si l'ordre de grandeur est inférieur à 0, si ce n'est pas un float

  - return 0 si l'ordre ne vaut pas 0.1, 0.01, 0.001 etc ... / les tests vérifient que ces valeurs est bien respectée

  - ne prend pas en compte l'ordre de grandeur dans le résultat si ce dernier est supérieur à 1 : dans ce cas là il renvoie la
    valeur de la fonction sans l'ordre de grandeur

  - l'ordre de grandeur défini doit être compris entre 0 et 1 avec 0 et 1 exclus

  - si le point défini est 0, la fonction renvoie 0 pour éviter les divisions par 0 

  - il y a 5 fonctions dans le fichier, 3 sont des polynomes et 2 sont des fonctions trigonométriques --> on pourrait en rajouter
    plus 