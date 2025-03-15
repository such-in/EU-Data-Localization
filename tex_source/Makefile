all: paper.pdf

paper.pdf: main.pdf
	cp main.pdf paper.pdf

main.pdf: *.tex references.bib
	pdflatex main.tex
	bibtex main
	pdflatex main.tex
	pdflatex main.tex

clean:
	rm -f paper.pdf main.pdf *.aux *.blg *.bbl *.log *.tmp *.xref *.idv *.4og *.4ct *.lg *.4tc *~
