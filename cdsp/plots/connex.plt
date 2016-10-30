# Output
set terminal png enhanced font "arial,10" fontscale 1.0
set output 'img/connex.png'

# Histogram settings
set style data boxes
set boxwidth 0.6 relative
set style fill solid 1.0

# Labels
set xlabel 'Seuil du graphe géométrique'
set ylabel 'Temps (ms)'

# Ranges and ticks
set yrange [ 0: ]
set xrange [ 2:66 ]
set xtics 5

# Plot
plot 'data/connex.dat' using 1:3 with boxes title ''