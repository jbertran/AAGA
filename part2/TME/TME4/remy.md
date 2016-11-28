# Algorithme de génération aléatoire uniforme d'arbres binaires incomplets

```
Noeuds ::= Feuille parent
        |  Unaire g d parent
        |  Binaire g d parent

gen n:
    
    racine = Feuille NULL
    noeuds = [ racine ]
    tot_noeuds = poids(racine)

    nouveau = NULL

    Tant que |noeuds| < n:
        noeud = alea(noeuds)
        choix = randInt(3)
        
        Si estFeuille(noeud):
            nouveau = Feuille NULL
        
            Si choix = 2:
                rajouter_au_dessus(noeud, nouveau)
            Sinon:
                rajouter_fils(noeud, nouveau, choix)
        Si estUnaire(noeud):
            nouveau = Feuille NULL
            choix = randInt(2)
            
            Si choix = 0:
                rajouter_fils(noeud, nouveau)
            Sinon:
                rajouter_au_dessus(noeud, nouveau)
        Sinon:        # noeud binaire
            rajouter_au_dessus(noeud, nouveau)
    
    tot_noeuds += 2
    noeuds += nouveau
```
