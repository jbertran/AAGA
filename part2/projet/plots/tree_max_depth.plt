# Output
set terminal pdf enhanced font "arial,10" fontscale 1.0 size 640, 480
set output 'imgs/tree_avg_depth.pdf'

set key left top
set title 'Maximum depth of trees with respect to tree size'

set xlabel 'Size'
set ylabel 'Maximum depth'

plot 'data/tree_max_depth.csv' using 1:2 title '' with points