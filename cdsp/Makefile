.PHONY: clean all

all: rapport

rapport: rapport.md
	pandoc rapport.md -H preamble.tex -o rapport.pdf --listings

clean:
	rm -rf *.log *.out *.aux
