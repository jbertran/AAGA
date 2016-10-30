# Output
set terminal png enhanced font "arial,10" fontscale 1.0
set output 'img/algos.png'

# Histogram settings
set style data boxes
set boxwidth 0.6 relative
set style fill solid 1.0

# Labels
set xlabel 'Nombre de points dans le nuage'
set ylabel 'Temps (ms)'

# Plot
plot 'data/algos.dat' u 1:2 w linespoint title 'S-MIS', 'data/algos.dat' u 1:3 w linespoint title 'Aléatoire', 'data/algos.dat' u 1:4 w linespoint title 'Local searching', 'data/algos.dat' u 1:5 w linespoint title 'Steiner'