all: test.pdf

test.pdf: test.tex header.tex text.tex
	lualatex test.tex

#build:
	#mkdir -p build

clean:
	#rm -rf build
	rm -rf test.pdf

.PHONY: all clean
