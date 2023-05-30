all: build/v700.pdf

build/v700.pdf: v700.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v700.tex
	lualatex  --output-directory=build v700.tex
	biber build/v700.bcf
	lualatex  --output-directory=build v700.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
