deploy: index.html

build: slides.html

index.html: slides.html
	cp slides.html index.html

slides.html: slides.Rmd
	Rscript -e "rmarkdown::render('slides.Rmd')"

clean:
	rm slides.html
