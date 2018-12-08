**Kata Markov Chain**
(travis link: https://travis-ci.org/YohannL)
Build a text generator based on a Markov Chain.


En français dans un premier temps
Faire un programme qui prend deux paramètres : un entier (pour demander un nombre de mots) et un texte (qui sert de base d’apprentissage); et qui génère un autre texte (de la longueur du paramètre.

Alternative : Il faut faire un logiciel en deux partie.
Une première partie qui analyse un texte pour en extraire des statistiques. Chaque mot doit avoir la liste des mots possible suivant avec un pourcentage d’apparition.
Par exemple avec ce texte : les hommes libres peuvent rester libres ou bien vendre leur liberté Nous devrions extraire quelque chose qui dirait:

"Les" est suivi par "hommes" à 100%
"hommes" est suivi par "libres" à 100%
"libres" est suivi par "peuvent" à 50% et "ou" à 50%
...

Une deuxième partie qui génère un texte à partir des statistiques précédente et d’un paramètre sur le nombre de mot du texte à générer. On peut envisager d’avoir un autre paramètre sur le premier mot du texte.

Example to try :
python main.py 5 "Windows talking painted pasture yet its express parties use. Sure last upon he same as knew next. Of believed or diverted no rejoiced. End friendship sufficient assistance can prosperous met. As game he show it park do. Was has unknown few certain ten promise. No finished my an likewise cheerful packages we. For assurance concluded son something depending discourse see led collected. Packages oh no denoting my advanced humoured. Pressed be so thought natural. "
