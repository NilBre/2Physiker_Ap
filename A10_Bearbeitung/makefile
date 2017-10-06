all: build/content.pdf

build/content.pdf: content.tex

build/content.pdf: FORCE | build
	TEXINPUTS="$(call translate,build:)" \
	BIBINPUTS=build: \
	max_print_line=1048576 \
latexmk \
--lualatex \
--output-directory=build \
--interaction=nonstopmode \
--halt-on-error \
content.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean FORCE
