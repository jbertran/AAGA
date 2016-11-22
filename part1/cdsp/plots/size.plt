# Output
set terminal png enhanced font "arial,10" fontscale 1.0 size 600, 400
set output 'img/size.png'

# Histogram settings
set style data boxes
set boxwidth 0.6 relative
set style fill solid 1.0

# Labels
set xlabel 'Nombre de points dans le nuage'
set ylabel 'Temps (ms)'

set yrange [ 0:950 ]

# Best fit line
f(x) = a*x+b
fit f(x) 'data/size.dat' using 1:3 via a,b
title_f(a,b) = sprintf('Régression linéaire: f(x) = %.2fx + %.2f', a, b)

# Plot
plot 'data/size.dat' using 1:3 with points title '', f(x) title title_f(a, b)