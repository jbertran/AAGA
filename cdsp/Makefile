.PHONY: clean all

all: rapport

rapport: rapport.md plots
	pandoc rapport.md -H preamble.tex -o rapport.pdf --listings

plots: connex # density size 

density: density.plt data/density.dat
	gnuplot density.plt

connex: connex.plt data/connex.dat
	gnuplot connex.plt

size: size.plt data/size.dat
	gnuplot size.plt

clean:
	rm -rf *.log *.out *.aux *.png
