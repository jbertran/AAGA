# Output
set terminal png enhanced font "arial,10" fontscale 1.0
set output 'times.png'

set key left top
set title 'Complexité temporelle expérimentale'

set xlabel 'Taille des arbres générés'
set ylabel 'Temps de génération moyen sur 50 instances (s)'

# Best fit line
f(x) = a*x**2+b*x+c
fit f(x) 'time_samples.dat' using 1:2 via a,b,c
title_f(a,b,c) = sprintf('Régression linéaire: f(x) = %.2fx**2 + %.2fx + %.2f', a, b, c)

plot 'time_samples.dat' using 1:2 title '' with linespoints, f(x) title title_f(a,b,c)