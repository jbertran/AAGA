.PHONY: all clean

all: tree_avg_node_depth.pdf tree_max_depth.pdf tree_avg_children.pdf tree_avg_time.pdf

%.pdf: data/%.csv plots/%.plt
	gnuplot $(word 2,$^)
