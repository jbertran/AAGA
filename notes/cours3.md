# AAGA - GA cours 3

## Génération aléatoire optimale (en nombre de bits alétoires nécessaires)

Soit $\mathcal{C}$ l'ensemble des objets d'un modèle. But: __générer__ (à partir d'un modèle de probas) un objet de \mathcal{C}.

Ex: un dé à 6 faces.

Implication:

__Générer un lanceur de dés__: renvoyer un entier entre 1 et 6, 'modèle probabiliste classique', chaque entier a la même probabilité d'apparaître (P = 1/6), distribution uniforme.

##### Propriété

Le nombre de bits alatoires nécessaires pour générer uniformément un objet de \mathcal{C} est au minimum $ \ceiling{log_2 \card{\mathcal{C}}} $

Remarque: pour générer uniformément chaque entier entre 1 et 6, on utilise 3 bits aléatoires uniformes.

Si on tombe sur, par exemple, 000 ou 111, il faut rejeter les 3 bits et recommencer. Ce n'est pas optimal.

### Génération d'un arbre binaire

Générer des arbres binaires dans \mathcal{C} = {arbres binaires de tailles 10 à 25} uniformément. Soit N = \card{\mathcal{C}}, on a au moins besoin de \ceiling{log N}.

Pour générer un objet de \mathcal{C} avec \ceiling{log_2 \card{\mathcal{C}}} bits aléatoires, on 'dessine' chaque objet de \mathcal{C} dans n'importe quel ordre, qu'on map avec une séquence de bits de \ceiling{log_2 \card{\mathcal{C}}}.

Il est garanti que le nombre de bits utilisé soit suffisant.

__But d'un générateur aléatoire__:

* économiser le nombre de bits nécessaires à la génération - on tente de s'approcher de l'optimal

## Arbres Binaires

Noeuds:

* soit une feuille
* soit un noeud interne, appelé racine, avec 2 fils (gauche et droit) qui sont tous deux des arbres binaires.

##### Spécifiation non ambigue

Règles de construction déterministes.

\mathcal{B} = Leaf | Node * \mathcal{B} * \mathcal{B}

On appelle taille d'un arbre le nombre de noeuds internes.

##### Propriété

Le nombre d'arbres binaires (arbres de Catalan) est le n-ième nombre de Catalan.

$$ Cat_n = \frac{1}{n+1} * 2n \parmi n  $$

$$ {Cat_n}_{n \geq 0} = {1, 1, 2, 5, 15, 42, .. } $$

Rappel: un arbre de taille n contient n+1 feuilles.

Un arbre de Catalan ne contient pas d'informations (pas de clés).

### Algorithme de Rémy

__But__: générer uniformément un arbre de Catalan de taille _n_ parmi l'ensemble des arbres de taille _n_.

Ex. Générer un des arbres de taille 3 avec une probabilité 1/5.

__Algo__:

* Point de départ: une feuille avec le numéro 1
* Supposons qu'on ait construit un arbre binaire binaire de taille k (k+1 feuilles numérotées de 1 à k+1).
  * On choisit uniformément un noeud de l'arbre (noeud interne ou feuille). Actuellement on a 2k + 1 noeuds, on en choisit un avec P = 1/2k+1
    On note \mathcal{F} l'arbre enraciné en ce noeud et \mathcal{A} l'arbre global de taille k.
  * On détache \mathcal{F} de \mathcal{A}.
  * On remplace \mathcal{F} par un noeud interne.
  * On tire à pile ou face:
    * Avec P = 1/2 on met F en fils gauche du nouveau noeud 
    * Avec P = 1/2 on met F en fils droit du nouveau noeud 
  * Le 2ème fils du nouveau noeud est une nouvelle feuille __k+2__
