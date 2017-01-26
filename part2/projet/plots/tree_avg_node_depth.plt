# Output
set terminal svg enhanced font "arial,10" size 300, 300
set output 'imgs/tree_avg_node_depth.svg'

set key left top
set title 'Average depth of nodes with respect to tree size'

set xlabel 'Size'
set ylabel 'Average node depth'

plot 'data/tree_avg_node_depth.csv' using 1:2 title '' with points