# Output
set terminal png enhanced font "arial,10" fontscale 1.0
set output 'bits.png'

set key left top
set title 'Complexité en bits aléatoires générés'

set xlabel 'Taille des arbres générés'
set ylabel 'Moyenne du nombre de bits aléatoires générés'

# Best fit line
f(x) = a*x+b
fit f(x) 'bits_samples.dat' using 1:2 via a,b
title_f(a,b) = sprintf('Régression linéaire: f(x) = %.2fx + %.2f', a, b)

plot 'bits_samples.dat' using 1:2 title '' with linespoints, f(x) title title_f(a, b)