# Output
set terminal svg enhanced font "arial,10" size 300, 300
set output 'imgs/tree_max_depth.svg'

set key left top
set title 'Maximum depth of trees with respect to tree size'

set xlabel 'Size'
set ylabel 'Maximum depth'

plot 'data/tree_max_depth.csv' using 1:2 title '' with points