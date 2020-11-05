# Test Waycom

Tests techniques de recrutement chez Waycom 

 - [Problème 1](#Contage-de-mots)
 - [Problème 2](#Pic-d’appels)


## Contage de mots

**Objectif :** Écrire un programme permettant de classer par nombre d’occurrences les
mots d’un texte capturé sur l’entrée standard.

Aucun module n'est autorisé, tout doit être fait à la main.
Vous vous attacherez à livrer cette réalisation comme vous le feriez dans une situation
classique de projet.

Exemples de résultats attendus :

```shell script
$ echo "foo bar baz foo" | ./comptage_mot.py
2 foo
1 bar
1 baz
```

```shell script
$ cat /etc/services | ./comptage_mot.py
581 #
65 Protocol
29 Service
21 private
[...]
```

## Pic d’appels

**Objectif :** Ecrire un programme qui lit une liste d'appels sur l’entrée standard. Cette liste
d'appels est une succession de lignes présentées sous la forme suivante :

**start:end**

"start" et "end" sont tous deux des integers, il s'agit de la date de début et de la date de
fin d'un appel, au format timestamp. "end" est strictement supérieur à " start ". Les lignes
sont triées sur le champ " start " par ordre croissant.

Voici un exemple :

1385718405:1385718491
1385718407:1385718409
1385718408:1385718452
1385718408:1385718464
1385718413:1385718452

Le programme doit afficher le pic d'appels, c'est à dire le nombre maximum d'appels
simultanés (actifs dans la même seconde) sur l’ensemble des appels recensés.

Exemple de résultat attendu :
```shell script
$ cat calls.txt
1385718405:1385718491
1385718407:1385718409
1385718408:1385718452
1385718408:1385718464
1385718413:1385718452
```

```shell script
$ cat calls.txt | ./pic_appel.py
4
```

Aucun module n'est autorisé, tout doit être fait à la main.

Vous vous attacherez à livrer cette réalisation comme vous le feriez dans une situation
classique de projet.
