# Output
set terminal pdf enhanced font "arial,10" fontscale 1.0 size 640, 480
set output 'imgs/tree_avg_time.pdf'

set key left top
set title 'Generation time of general trees with respect to size'

set xlabel 'Size'
set ylabel 'Generation time'

plot 'data/tree_avg_time.csv' using 1:2 title '' with points