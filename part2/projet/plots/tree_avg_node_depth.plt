# Output
set terminal pdf enhanced font "arial,10" fontscale 1.0 size 640, 480
set output 'imgs/tree_avg_node_depth.pdf'

set key left top
set title 'Average depth of nodes with respect to tree size'

set xlabel 'Size'
set ylabel 'Average node depth'

plot 'data/tree_avg_node_depth.csv' using 1:2 title '' with points