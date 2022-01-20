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
  - return un string avec un espace, si on donne un string avec un espace en entrée