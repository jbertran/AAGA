.PHONY: clean all

all: rapport

rapport: rapport.md plots
	pandoc rapport.md -H preamble.tex -o rapport.pdf --listings

plots: connex density # size 

density: plots/density.plt data/density.dat
	gnuplot plots/density.plt

connex: plots/connex.plt data/connex.dat
	gnuplot plots/connex.plt

size: plots/size.plt data/size.dat
	gnuplot plots/size.plt

clean:
	rm -rf *.log *.out *.aux *.png
