%Rapport sur l'algorithme de calcul d'Ensemble dominant connexe minimal présenté dans l'article *On greedy construction of connected dominating sets in wireless networks* de Li, Thai, Wang, Yi, Wan, Du, Tong, Bin, Zao, Wun, Zhou, 2005 (1).
%Darius Mercadier \and Jordi Bertran de Balanda

Rapport sur l'algorithme de calcul d'Ensemble dominant connexe minimal présenté dans l'article *On greedy construction of connected dominating sets in wireless networks* de Li, Thai, Wang, Yi, Wan, Du, Tong, Bin, Zao, Wun, Zhou, 2005 (1).

===

# Introduction
Un ensemble dominant d'un graphe *G* = (*S*, *A*) est un sous-ensemble *D* de *S* tel que pour toute arrête *uv* $\in$ *A*, *u* $\in$ *D* ou *v* $\in$ *D*. Le problème consistant à trouver un ensemble dominant connexe de taille minimal (MCDS) est NP-Difficile. Dans ce rapport, nous étudierons l'algortihme *S-MIS* présenté dans *On greedy construction of connected dominating sets in wireless networks* de Li, Thai, Wang, Yi, Wan, Du, Tong, Bin, Zao, Wun, Zhou, 2005, qui propose un Schema d'approximation en temps polynomial (PTAS) donnant une *(4.8+ln(5))*-approximation de la solution optimale. Nous commenceront par présenter l'algorithme, puis présenteront les résultats expérimentaux obtenus, que nous compareront avec d'autres algorithmes de résolution de ce problème.

Plus précisémment, nous étudieront cette algorithme dans le contexte des graphes géométriques. Ceux-ci sont composés d'un ensemble de sommets *S* et d'arrêtes *A* telles que *uv* $\in$ *A* si et seulement si *distance(u,v)* $\leq$ *k*, *k* étant un seuil fixe. Nous présenteront également les générateurs aléatoires utilisés pour générer les graphes de tests.  


# Présentation de l'algorithme

L'algorithme *S-MIS* consiste en deux étapes : le calcul d'un *Maximum Independent Set* (MIS), puis le calcul du MCDS.

Le papier présentant l'algorithme *S-MIS* ne présente pas d'algorithme permettant le calcul du MIS, mais suggère deux approches de calcul (2,3). Nous avons donc implémenté l'algorithme de Wan, Alzoubi et Frieder (3).

## 1- Calcul du MIS

Un ensemble indépendant dans un graphe *G* = (*S*, *A*) est un sous-ensemble *D* de *S* tel que pour tout *u* $\in$ *D* et *v* $\in$ *D*, *uv* $\notin$ *A*. Le problème de calculer un ensemble indépendant maximum est NP-difficile. C'est donc sur une $\alpha$-approximation que nous avons implémenté.  
Le MIS nécessaire au calcul du MCDS avec l'algorithme S-MIS doit de plus satisfaire une condition supplémentaire : pour tout *u* $\in$ *D*, il doit exister *w* $\in$ *S* tel qu'il existe *v* $\in$ *D*, *v* $\neq$ *u* tel que *uw* $\in$ *A* et *vw* $\in$ *A*. Moins formellement, cela signifie qu'entre deux points apparetenant au MIS, il doit y avoir un et un seul point n'appartenant pas au MIS.

![Un MIS valide comme base de l'algorithme S-MIS](img/fig1.png)

![Un MIS invalide comme base de l'algorithme S-MIS](img/fig2.png)


Les figures 1 et 2 montrent toutes les deux des MIS : tous les sommets sont soit dans le MIS soit ont un voisin dans le MIS, et aucun sommet du MIS n'a de voisin dans le MIS. Cependant, dans le second, les deux sommets du MIS sont séparés d'une distance de deux sommets tandis qu'il ne sont séparés que d'un sommet dans le premier. Par conséquent, seule la figure 1 représente un MIS valide comme base de l'algorithme S-MIS.  


### Implémentation de l'algorithme de calcul du MIS
L'algorithme utilisé pour calculer le MIS se base sur un système de couleur pour différencier les points non-visités (blancs) des points appartenant au MIS (noirs) et des points n'appartenant pas au MIS (bleus) : on part d'un point au hasard du graphe, que l'on marque noir (il est le premier point du MIS). On marque tous ses voisins bleus (il ne peuvent pas appartenir au MIS). Puis on ajoute les voisins des voisins qui sont encore blancs à la liste des points potentiellement dans le MIS. On retire le premier point de cette liste et on réitère le processus tant qu'il reste des points à examiner.  
De manière plus pratique, le pseudo-code de cet algorithme est le suivant : 

    def MIS ( G = (V,E) ) :
	  MIS = []
	  for (p : V) :                     # Initializing the colors.
	    p.color = White
	  
	  Stack = [V.pop]
	  while (Stack.notEmpty) :
	    current = Stack.pop
		if (current.color == Blue) :    # Already covered
		  continue
		current.color = Black           # Adding it to the MIS
		MIS.add(current)
	    
		for (p : current.neighbors) :
		  p.color == Blue               # Marking the neighbors as covered
	  
	    for (p : current.neighbors) :
		  for (q : p.neighbors) :
		    if (q.color == White) :     # Adding the neighbors of the neighbors
			  Stack.add(q)              #  to the potential points of the MIS.
	
	  return MIS
	  
### Complexité du calcul du MIS

On note *n*=|*S*|, et *m*=|*E*|.  

__Initialisation__ :  
Initialiser les couleurs des sommets requière un unique parcours des sommets, en temps linéaire en la taille de *S* : `O(n)`.  
Pour des questions d'optimisation, on précalculera lors de l'initialisation une table d'association point-voisins qui a chaque point associera ses voisins. Cette opération est réalisable en `O(n*m)`), et permet de réaliser l'opération `neihbors` en `O(1)`.

__Boucle principale__ :  
Le pseudo-code précédemment donné est une version simplifié de l'algorithme réel pour des raisons de lisibilité, en particulier, dans une vrai implémentation un point n'est ajouté à la stack que si il n'y est pas déjà et si il est blanc. En tenant compte de cette condition, et en constatant qu'il y a autant d'itération de la boucle principale qu'il y a d'éléments qui sont ajoutés dans la stack lors de l'execution de l'algorithme, et vu qu'un sommet blanc enlevé de la Stack est marqué noir, on en conclue que le nombre d'itéreation de cette boucle est borné par *n*.  
On a expliqué précédemment que l'opération `neighbors` est réalisable en temps constant. Le nombre de voisins d'un points cependant est uniquement bornée par *m*. Par conséquent la boucle parcourant les voisins des voisins a une complexité en `O(m*m)`.  
La complexité de la boucle principale est donc `O(n*m*m)`.  

Il convient cependant de noter que dans les instances traitées, cette limite est une sur-approximation très large. En effet, les graphes étant géométriques, la distribution des sommets aléatoire et uniforme, et le seuil *k* très inférieur à la distance entre les extrèmes du domaine de définition des sommets, le nombre d'arrête par sommets sera très inférieur à *m*.  
Par conséquent, une complexité plus réaliste serait de l'ordre de `O(n*m)`. (Celà revient à supposer que le nombre d'arrêtes par sommets est de l'ordre de $\sqrt{m}$; ce chiffre dépend en réalité de la quantité de sommets, de l'air de la surface dans laquelle ils sont, et de l'uniformité de leur répartition. Dans nos test, ce chiffre $\sqrt{m}$ est raisonnable).




## 2- Calcul du S-MIS



# Références

1. Yingshu Li, My T. Thai, Feng Wang, Chih-Wei Yi, Peng-Jun Wan and Ding-Zhu Du, On greedy construction of connected dominating sets in wireless networks, 2005.
2. Cadei M, Cheng MX, Cheng X, Du D-Z. Connected domination in ad hoc wireless networks. In Proceedings of the 6th International Conference on Computer Science and Informatics (CS&I’2002), Durham, NC, USA, March, 2002.
3. Wan P-J, Alzoubi KM, Frieder O. Distributed construction of connected dominating set in wireless ad hoc networks. In Proceedings of IEEE Infocom 2002, New York, NY, USA, June 2002.
