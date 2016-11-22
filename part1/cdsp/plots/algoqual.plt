# Output
set terminal png enhanced font "arial,10" fontscale 1.0
set output 'img/algoqual.png'

# Legend
set key left top

# Labels
set xlabel 'Nombre de points dans le nuage'
set ylabel 'Taille du CDS résultat'

# Plot
plot for [COL=2:5] 'data/algoqual.dat' using 1:COL title columnheader with linespoints 