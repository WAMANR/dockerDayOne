# Cours Docker

Ce repository comprends le Tp1, le Tp2 ainsi que le devoir de fin de semaine pour le cours de Docker.

## Commande 

* ./build.sh
  build les images et le network
* ./run.sh 1000 10 10 10 10
  lance les conteneurs avec comme paramètres (port de départ des workers, tasks, workers généraux, workers addition, workers multiplication)
* ./stop.sh
  stop et supprime les images ainsi que le network


## Fabriqué avec

* [Docker](https://www.docker.com/) - Conteneurisation du projet
* [Visual Studio code](https://code.visualstudio.com/) - Editeur de textes

## Evaluation

* Exercice 1: https://github.com/WAMANR/dockerDayOne/commit/6230666f526994fa3efb7f2f934731ef37235f7a

J'ai ajouté un Dockerfile pour le planner et un autre pour le worker. J'ai créer 3 fichiers : build.sh, run.sh et stop.sh qui respectivement build les images, les lancent et les stoppent. Pour pouvoir exécuter 4 tâches j'ai tout simplement passé au run du planner la variable environnement TASKS=4.
De plus, j'ai ajouté un worker dans la variable workers du planner.

* Exercice 2: https://github.com/WAMANR/dockerDayOne/commit/aab63f75d586f5038a12f439ef3748af80e41143

J'ai dans la liste workers du planner un deuxième worker avec un port différent. J'ai, dans le run.sh, lancé un deuxième worker avec le nom et le port différent indiqué dans le planner. Les deux effectuent deux taches chacun.

* Exercice 3: 

-On remarque des erreurs car des mult sont envoyées au worker add et inversement.
-Pour corriger cela, j'ai ajouté une condition qui vérifie si le type de tache correspond au worker disponible.

* Exercice 4 et 5:
-J'ai ajouté un type "gen" qui peut être appelé pour la multiplication et l'addition.
-J'ai ajouté un script shell qui permet de créer les conteneurs des workers (généraux, multiplication et addition) de manière dynamique (selon des variables) et qui transmet la liste des ports au planner.
-J'ai ajouté des parties de code qui permettent de construire les workers à partir de la liste de ports.

CEPENDANT, CELA NE FONCTIONNE PAS PAR FAUTE DE TEMPS MAIS JE SUIS VRAIMENT PRES DU BUT. UN PEU DE DEBUGGING ET MON CODE FONCTIONNE J'IMAGINE...

## Auteur
* **Adil Rouichi** _alias_ [@WAMANR](https://github.com/WAMANR)

