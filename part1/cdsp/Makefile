.PHONY: clean all

all: rapport

rapport: rapport.md plots
	pandoc rapport.md --variable documentclass=article --variable classoption=titlepage -H preamble.tex -o rapport.pdf --listings --number-sections --toc

plots: connex size algos

connex: plots/connex.plt data/connex.dat
	gnuplot plots/connex.plt

size: plots/size.plt data/size.dat
	gnuplot plots/size.plt

algos: plots/algos.plt data/algos.dat
	gnuplot plots/algos.plt

clean:
	rm -rf *.log *.out *.aux *.png
