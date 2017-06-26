TEX = latexmk -f -pdf -shell-escape -interaction=nonstopmode -file-line-error
PANDOC = pandoc -s -S 
PREVIEW = open -a /Applications/Preview.app
#PLANTUML = plantuml -tlatex
PLANTUML = plantuml
BASEDIR = `pwd`

all: compile view
	echo 'ok'

thesis: images compile clean view 
	echo 'ok'

compile:
	$(TEX) dissertacao-vitor.tex

images:
	cd figuras/fontes; \
	$(TEX) *; \
	mv *.pdf ../graficos/;

expand:
	latexpand dissertacao-vitor.tex > tmpdissertacao.tex

dev: expand
	$(TEX) tmpdissertacao.tex
	mv tmpdissertacao.pdf builds/dev-`date '+%Y%M%d'`-dissertacao.pdf
	-rm tmpdissertacao.*

uml:
	cd figuras/uml; \
	$(PLANTUML) *.puml; \
	mv *.png ../graficos/;

view:
	$(PREVIEW) dissertacao-vitor.pdf

clean:
	-rm -f figuras/fontes/*.aux
	-rm -f figuras/fontes/*.
	-rm -f figuras/fontes/*.fdb_latexmk
	-rm -f figuras/fontes/*.fls
	-rm -f figuras/fontes/*.log
	-rm -f *.aux *.bbl *.blg *.brf *.fdb_latexmk *.fls
	-rm -f *.idx *.ilg *.ind *.loa *.lof *.log *.lot
	-rm -f *.synctex.gz *.toc *.nav *.out *.snm *.lol
	-rm -rf _minted-*
