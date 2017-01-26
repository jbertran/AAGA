.PHONY: all clean

SVGS=tree_avg_node_depth.svg tree_max_depth.svg tree_avg_children.svg tree_avg_time.svg
PDFS=${SVGS:.svg=.pdf}

all: $(PDFS)

%.pdf: %.svg
	inkscape -D -z --file=imgs/$^ --export-pdf=imgs/$@ --export-latex

%.svg: data/%.csv plots/%.plt
	gnuplot $(word 2,$^)

run:
	python3 projet.py
