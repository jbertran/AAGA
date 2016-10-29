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

set yrange [ 0: ]

# Plot
plot 'data/size.dat' using 1:3 with boxes title ''