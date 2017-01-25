.PHONY: all clean

all: tree_avg_node_depth.pdf tree_avg_depth.pdf tree_avg_children.pdf

%.pdf: data/%.csv plots/%.plt
	gnuplot $(word 2,$^)
