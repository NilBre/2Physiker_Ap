all: Task6.pdf

Task6.pdf: header06.tex Task6.tex table.tex table2.tex savart.tex gauss.tex Maxwell.tex ebenwelle.tex welle.tex oszi.tex
	lualatex Task6.tex

clean:
	rm -rf Task6.pdf

.PHONY:
	all clean
