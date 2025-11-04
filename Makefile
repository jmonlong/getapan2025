deploy: 
	cp slides.html index.html

build:
	Rscript -e "rmarkdown::render('slides.Rmd')"
