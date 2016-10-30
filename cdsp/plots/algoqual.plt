# Output
set terminal png enhanced font "arial,10" fontscale 1.0
set output 'img/algoqual.png'

# Legend
set key left top

# Histogram settings
set style data histogram
set style histogram clustered
set boxwidth 0.6 relative
set style fill solid 1.0

# Labels
set xlabel 'Nombre de points dans le nuage'
set ylabel 'Taille du CDS résultat'

# Plot
plot for [COL=2:5] 'data/algoqual.dat' using COL:xticlabels(1) title columnheader