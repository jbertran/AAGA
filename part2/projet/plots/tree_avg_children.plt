# Output
set terminal svg enhanced font "arial,10" size 300, 300
set output 'imgs/tree_avg_children.svg'

set key left top
set title 'Average number of node children with respect to tree size'

set xlabel 'Size'
set ylabel 'Average number of node children'

plot 'data/tree_avg_children.csv' using 1:2 title '' with points