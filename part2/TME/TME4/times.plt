# Output
set terminal png enhanced font "arial,10" fontscale 1.0
set output 'times.png'

set key left top
set title 'Complexité temporelle expérimentale'

set xlabel 'Taille des arbres générés'
set ylabel 'Temps de génération moyen sur 50 instances (s)'

plot 'time_samples.dat' using 1:2 title '' with linespoints