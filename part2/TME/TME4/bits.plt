# Output
set terminal png enhanced font "arial,10" fontscale 1.0
set output 'bits.png'

set key left top
set title 'Complexité en bits aléatoires générés'

set xlabel 'Taille des arbres générés'
set ylabel 'Moyenne du nombre de bits aléatoires générés'

plot 'bits_samples.dat' using 1:2 title '' with linespoints