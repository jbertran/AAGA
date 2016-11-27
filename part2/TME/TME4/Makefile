.PHONY: all

all: plots

plots: timeplot bitsplot

timeplot: times.plt time_samples.dat
	gnuplot times.plt

bitsplot: bits.plt bits_samples.dat
	gnuplot bits.plt

data: bitsdata timedata

timedata:
	./randomTrees.py --benchtime

bitsdata:
	./randomTrees.py --benchbits
