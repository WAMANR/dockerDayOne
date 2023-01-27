# Cours Docker

Ce repository comprends le Tp1, le Tp2 ainsi que le devoir de fin de semaine pour le cours de Docker.

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

-

## Auteur
* **Adil Rouichi** _alias_ [@WAMANR](https://github.com/WAMANR)

