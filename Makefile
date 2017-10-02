all: hello.pdf

hello.pdf: hello.tex Teil1.tex header.tex list.tex pers.tex Versuch.tex
	lualatex hello.tex

#build:
	#mkdir -p build

clean:
	#rm -rf build
	rm -rf hello.pdf

.PHONY: all clean
