# Output
set terminal svg enhanced font "arial,10" size 300, 300
set output 'imgs/tree_avg_time.svg'

set key left top
set title 'Generation time of general trees with respect to size'

set xlabel 'Size'
set ylabel 'Generation time'

plot 'data/tree_avg_time.csv' using 1:2 title '' with points