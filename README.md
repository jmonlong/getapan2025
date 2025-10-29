See [revealjs.cheatsheet.md](revealjs.cheatsheet.md) for syntax cheatsheet.

## Compile HTML

```r
rmarkdown::render('slides.Rmd')
```

Then open [slides.html](slides.html) in a browser.

## Export to PDF

1. Open and add `?print-pdf` in address bar
1. Print as PDF (Ctrl-P)
2. Optional: 
    3. Margins = None.
    4. Background enabled

## "Animations"

Maybe we could remove the transition effect and use "vertical" slides?

That means using, in the header:

- `transition: none`
- `slide_level: 2` and using `##` for vertical slides

If we are bothered by having to press *down* to go through the animations, we could add `navigationMode: linear` which makes *right* go through the sub-slides (as usual)


## Custom styles

Defined in `styles.css` and used by adding a *class* tag to elements.

### Control image display

```md
![](hprc-tubemap.jpeg){.himg .simg}
```

With:

- `.half_wide_img`: half as wide as the slide, max 400px high
- `.wide_img`: just max 400px high
- `.shadow_img`: box shadow

### Citing a paper

```md
<div class="cite">
Liao, Asri, Ebler, et al. Nature 2023
</div>
```

### Adding a small legend

```md
<div class="legend">
\**json* representation
</div>
```
