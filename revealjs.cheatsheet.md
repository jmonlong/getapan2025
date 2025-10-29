R Markdown Format for reveal.js Presentations
================

<!-- badges: start -->

[![CRAN
status](https://www.r-pkg.org/badges/version/revealjs)](https://CRAN.R-project.org/package=revealjs)
[![R-CMD-check](https://github.com/rstudio/revealjs/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/rstudio/revealjs/actions/workflows/R-CMD-check.yaml)
[![reveal.js](https://img.shields.io/badge/reveal.js-4.2.1-yellow)](https://github.com/rstudio/revealjs/tree/main/inst/reveal.js-4.2.1)
<!-- badges: end -->

## Overview

This repository provides an [R Markdown](http://rmarkdown.rstudio.com)
custom format for [reveal.js](https://revealjs.com/) HTML presentations.
The packages includes *reveal.js* library in version 4.2.1

You can use this format in R Markdown documents by installing this
package as follows:

``` r
install.packages("revealjs")
```

To create a [reveal.js](https://revealjs.com/) presentation from R
Markdown you specify the `revealjs_presentation` output format in the
front-matter of your document. You can create a slide show broken up
into sections by using the `#` and `##` heading tags (you can also
create a new slide without a header using a horizontal rule (`----`).
For example here’s a simple slide show:

``` markdown
---
title: "Habits"
author: John Doe
date: March 22, 2005
output: revealjs::revealjs_presentation
---

# In the morning

## Getting up

- Turn off alarm
- Get out of bed

## Breakfast

- Eat eggs
- Drink coffee

# In the evening

## Dinner

- Eat spaghetti
- Drink wine

## Going to sleep

- Get in bed
- Count sheep
```

## Rendering

Depending on your use case, there are 3 ways you can render the
presentation.

1.  RStudio
2.  R console
3.  Terminal (e.g., bash)

### RStudio

When creating the presentation in RStudio, there will be a `Knit` button
right below the source tabs. By default, it will render the current
document and place the rendered `HTML` file in the same directory as the
source file, with the same name.

### R Console

The `Knit` button is actually calling the `rmarkdown::render()`
function. So, to render the document within the R console:

``` r
rmarkdown::render('my_reveal_presentation.Rmd')
```

There are many other output tweaks you can use by directly calling
`render`. You can read up on the
[documentation](https://pkgs.rstudio.com/rmarkdown/reference/render.html)
for more details.

### Command Line

When you need the presentation to be rendered from the command line:

``` bash
Rscript -e "rmarkdown::render('my_reveal_presentation.Rmd')"
```

## Display Modes

The following single character keyboard shortcuts enable alternate
display modes:

- `'f'` enable fullscreen mode

- `'o'` enable overview mode

- `'b'` enable pause mode with a black screen hiding slide content

- `'?'` enable help mode to show keyboard shortcut cheatsheet

- `'s'` enable presentation mode with speaker notes when the Notes
  plugin is activated

- `'m'` enable menu mode when the ‘menu’ plugin is activated

Pressing `Esc` exits all of these modes.

## Incremental Bullets

You can render bullets incrementally by adding the `incremental` option:

``` yaml
---
output:
  revealjs::revealjs_presentation:
    incremental: true
---
```

If you want to render bullets incrementally for some slides but not
others you can use this syntax:

``` markdown
::: incremental

- Eat spaghetti
- Drink wine

:::
```

or

``` markdown
::: nonincremental

- Eat spaghetti
- Drink wine

:::
```

## Incremental Revealing

You can also add pauses between content on a slide using `. . .`

``` markdown
# Slide header

Content shown first

. . .

Content shown next on the same slide
```

Using Fragments explicitly is also possible

``` markdown
# Slide header

Content shown first

::: fragment
Content shown next on the same slide
:::
```

## Appearance and Style

There are several options that control the appearance of revealjs
presentations:

- `theme` specifies the theme to use for the presentation (available
  themes are “simple”, “dark”, “black”, “sky”, “beige”, “serif”,
  “solarized”, “blood”, “moon”, “night”, “league”, or “white”

- `highlight` specifies the syntax highlighting style. Supported styles
  include “default”, “tango”, “pygments”, “kate”, “monochrome”,
  “espresso”, “zenburn”, “haddock”, or “breezedark”. Pass null to
  prevent syntax highlighting.

- `center` specifies whether you want to vertically center content on
  slides (this defaults to false).

For example:

``` yaml
output:
  revealjs::revealjs_presentation:
    theme: sky
    highlight: pygments
    center: true
```

[Revealjs documentation about themes](https://revealjs.com/themes/)

## Slide Transitions

You can use the `transition` and `background_transition` options to
specify the global default slide transition style:

- `transition` specifies the visual effect when moving between slides.
  Available transitions are “convex”, “fade”, “slide”, “concave”,
  “zoom”, or “none”.

- `background_transition` specifies the background transition effect
  when moving between full page slides. Available transitions are
  “convex”, “fade”, “slide”, “concave”, “zoom”, or “none”

For example:

``` yaml
output:
  revealjs::revealjs_presentation:
    transition: fade
    background_transition: slide
```

You can override the global transition for a specific slide by using the
data-transition attribute, for example:

``` markdown
## Use a zoom transition {data-transition="zoom"}

## Use a faster speed {data-transition-speed="fast"}
```

You can also use different in and out transitions for the same slide,
for example:

``` markdown
## Fade in, Slide out {data-transition="slide-in fade-out"}

## Slide in, Fade out {data-transition="fade-in slide-out"}
```

This works also for background transition

``` markdown
## Use a zoomed background transition {data-background-transition="zoom"}
```

[Revealjs documentation about
transitions](https://revealjs.com/transitions/)

## Slide Backgrounds

Slides are contained within a limited portion of the screen by default
to allow them to fit any display and scale uniformly. You can apply full
page backgrounds outside of the slide area by adding a data-background
attribute to your slide header element. Four different types of
backgrounds are supported: color, image, video and iframe. Below are a
few examples.

``` markdown
## CSS color background {data-background-color=#ff0000}

## Full size image background {data-background-image="background.jpeg"}

## Video background {data-background-video="background.mp4"}

## Embed a web page as a background {data-background-iframe="https://example.com"}
```

Backgrounds transition using a fade animation by default. This can be
changed to a linear sliding transition by specifying the
`background-transition: slide`. Alternatively you can set
`data-background-transition` on any slide with a background to override
that specific transition.

[Revealjs documentation about
backgrounds](https://revealjs.com/backgrounds/)

## 2-D Presentations

You can use the `slide_level` option to specify which level of heading
will be used to denote individual slides. If `slide_level` is 2 (the
default), a two-dimensional layout will be produced, with level 1
headers building horizontally and level 2 headers building vertically.
For example:

``` markdown
# Horizontal Slide 1

## Vertical Slide 1

## Vertical Slide 2

# Horizontal Slide 2
```

With this layout horizontal navigation will proceed directly from
“Horizontal Slide 1” to “Horizontal Slide 2”, with vertical navigation
to “Vertical Slide 1”, etc. presented as an option on “Horizontal Slide
1”. Global reveal option
[`navigationMode`](https://revealjs.com/vertical-slides/#navigation-mode)
can be tweaked to change this behavior.

## Reveal Options

Reveal.js has many additional options to configure it’s behavior. You
can specify any of these options using `reveal_options`, for example:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    self_contained: false
    reveal_options:
      slideNumber: true
      previewLinks: true
---
```

You can find documentation on the various available Reveal.js options
here: <https://revealjs.com/config/>.

```js
Reveal.initialize({
  // Display presentation control arrows
  controls: true,

  // Help the user learn the controls by providing hints, for example by
  // bouncing the down arrow when they first encounter a vertical slide
  controlsTutorial: true,

  // Determines where controls appear, "edges" or "bottom-right"
  controlsLayout: 'bottom-right',

  // Visibility rule for backwards navigation arrows; "faded", "hidden"
  // or "visible"
  controlsBackArrows: 'faded',

  // Display a presentation progress bar
  progress: true,

  // Display the page number of the current slide
  // - true:    Show slide number
  // - false:   Hide slide number
  //
  // Can optionally be set as a string that specifies the number formatting:
  // - "h.v":   Horizontal . vertical slide number (default)
  // - "h/v":   Horizontal / vertical slide number
  // - "c":   Flattened slide number
  // - "c/t":   Flattened slide number / total slides
  //
  // Alternatively, you can provide a function that returns the slide
  // number for the current slide. The function should take in a slide
  // object and return an array with one string [slideNumber] or
  // three strings [n1,delimiter,n2]. See #formatSlideNumber().
  slideNumber: false,

  // Can be used to limit the contexts in which the slide number appears
  // - "all":      Always show the slide number
  // - "print":    Only when printing to PDF
  // - "speaker":  Only in the speaker view
  showSlideNumber: 'all',

  // Use 1 based indexing for # links to match slide number (default is zero
  // based)
  hashOneBasedIndex: false,

  // Add the current slide number to the URL hash so that reloading the
  // page/copying the URL will return you to the same slide
  hash: false,

  // Flags if we should monitor the hash and change slides accordingly
  respondToHashChanges: true,

  // Enable support for jump-to-slide navigation shortcuts
  jumpToSlide: true,

  // Push each slide change to the browser history.  Implies `hash: true`
  history: false,

  // Enable keyboard shortcuts for navigation
  keyboard: true,

  // Optional function that blocks keyboard events when retuning false
  //
  // If you set this to 'focused', we will only capture keyboard events
  // for embedded decks when they are in focus
  keyboardCondition: null,

  // Disables the default reveal.js slide layout (scaling and centering)
  // so that you can use custom CSS layout
  disableLayout: false,

  // Enable the slide overview mode
  overview: true,

  // Vertical centering of slides
  center: true,

  // Enables touch navigation on devices with touch input
  touch: true,

  // Loop the presentation
  loop: false,

  // Change the presentation direction to be RTL
  rtl: false,

  // Changes the behavior of our navigation directions.
  //
  // "default"
  // Left/right arrow keys step between horizontal slides, up/down
  // arrow keys step between vertical slides. Space key steps through
  // all slides (both horizontal and vertical).
  //
  // "linear"
  // Removes the up/down arrows. Left/right arrows step through all
  // slides (both horizontal and vertical).
  //
  // "grid"
  // When this is enabled, stepping left/right from a vertical stack
  // to an adjacent vertical stack will land you at the same vertical
  // index.
  //
  // Consider a deck with six slides ordered in two vertical stacks:
  // 1.1    2.1
  // 1.2    2.2
  // 1.3    2.3
  //
  // If you're on slide 1.3 and navigate right, you will normally move
  // from 1.3 -> 2.1. If "grid" is used, the same navigation takes you
  // from 1.3 -> 2.3.
  navigationMode: 'default',

  // Randomizes the order of slides each time the presentation loads
  shuffle: false,

  // Turns fragments on and off globally
  fragments: true,

  // Flags whether to include the current fragment in the URL,
  // so that reloading brings you to the same fragment position
  fragmentInURL: true,

  // Flags if the presentation is running in an embedded mode,
  // i.e. contained within a limited portion of the screen
  embedded: false,

  // Flags if we should show a help overlay when the question-mark
  // key is pressed
  help: true,

  // Flags if it should be possible to pause the presentation (blackout)
  pause: true,

  // Flags if speaker notes should be visible to all viewers
  showNotes: false,

  // Global override for autolaying embedded media (video/audio/iframe)
  // - null:   Media will only autoplay if data-autoplay is present
  // - true:   All media will autoplay, regardless of individual setting
  // - false:  No media will autoplay, regardless of individual setting
  autoPlayMedia: null,

  // Global override for preloading lazy-loaded iframes
  // - null:   Iframes with data-src AND data-preload will be loaded when within
  //           the viewDistance, iframes with only data-src will be loaded when visible
  // - true:   All iframes with data-src will be loaded when within the viewDistance
  // - false:  All iframes with data-src will be loaded only when visible
  preloadIframes: null,

  // Can be used to globally disable auto-animation
  autoAnimate: true,

  // Optionally provide a custom element matcher that will be
  // used to dictate which elements we can animate between.
  autoAnimateMatcher: null,

  // Default settings for our auto-animate transitions, can be
  // overridden per-slide or per-element via data arguments
  autoAnimateEasing: 'ease',
  autoAnimateDuration: 1.0,
  autoAnimateUnmatched: true,

  // CSS properties that can be auto-animated. Position & scale
  // is matched separately so there's no need to include styles
  // like top/right/bottom/left, width/height or margin.
  autoAnimateStyles: [
    'opacity',
    'color',
    'background-color',
    'padding',
    'font-size',
    'line-height',
    'letter-spacing',
    'border-width',
    'border-color',
    'border-radius',
    'outline',
    'outline-offset',
  ],

  // Controls automatic progression to the next slide
  // - 0:      Auto-sliding only happens if the data-autoslide HTML attribute
  //           is present on the current slide or fragment
  // - 1+:     All slides will progress automatically at the given interval
  // - false:  No auto-sliding, even if data-autoslide is present
  autoSlide: 0,

  // Stop auto-sliding after user input
  autoSlideStoppable: true,

  // Use this method for navigation when auto-sliding (defaults to navigateNext)
  autoSlideMethod: null,

  // Specify the average time in seconds that you think you will spend
  // presenting each slide. This is used to show a pacing timer in the
  // speaker view
  defaultTiming: null,

  // Enable slide navigation via mouse wheel
  mouseWheel: false,

  // Opens links in an iframe preview overlay
  // Add `data-preview-link` and `data-preview-link="false"` to customise each link
  // individually
  previewLinks: false,

  // Exposes the reveal.js API through window.postMessage
  postMessage: true,

  // Dispatches all reveal.js events to the parent window through postMessage
  postMessageEvents: false,

  // Focuses body when page changes visibility to ensure keyboard shortcuts work
  focusBodyOnPageVisibilityChange: true,

  // Transition style
  transition: 'slide', // none/fade/slide/convex/concave/zoom

  // Transition speed
  transitionSpeed: 'default', // default/fast/slow

  // Transition style for full page slide backgrounds
  backgroundTransition: 'fade', // none/fade/slide/convex/concave/zoom

  // The maximum number of pages a single slide can expand onto when printing
  // to PDF, unlimited by default
  pdfMaxPagesPerSlide: Number.POSITIVE_INFINITY,

  // Prints each fragment on a separate slide
  pdfSeparateFragments: true,

  // Offset used to reduce the height of content within exported PDF pages.
  // This exists to account for environment differences based on how you
  // print to PDF. CLI printing options, like phantomjs and wkpdf, can end
  // on precisely the total height of the document whereas in-browser
  // printing has to end one pixel before.
  pdfPageHeightOffset: -1,

  // Number of slides away from the current that are visible
  viewDistance: 3,

  // Number of slides away from the current that are visible on mobile
  // devices. It is advisable to set this to a lower number than
  // viewDistance in order to save resources.
  mobileViewDistance: 2,

  // The display mode that will be used to show slides
  display: 'block',

  // Hide cursor if inactive
  hideInactiveCursor: true,

  // Time before the cursor is hidden (in ms)
  hideCursorTime: 5000,
});
```

## Figure Options

There are a number of options that affect the output of figures within
reveal.js presentations:

- `fig_width` and `fig_height` can be used to control the default figure
  width and height (7x5 is used by default)

- `fig_retina` Specifies the scaling to perform for retina displays
  (defaults to 2, which currently works for all widely used retina
  displays). Note that this only takes effect if you are using knitr \>=
  1.5.21. Set to `null` to prevent retina scaling.

- `fig_caption` controls whether figures are rendered with captions

For example:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    fig_width: 7
    fig_height: 6
    fig_caption: true
---
```

## MathJax Equations

By default [MathJax](http://www.mathjax.org/) scripts are included in
reveal.js presentations for rendering LaTeX and MathML equations. You
can use the `mathjax` option to control how MathJax is included:

- Specify “default” to use an https URL from the official MathJax CDN.

- Specify “local” to use a local version of MathJax (which is copied
  into the output directory). Note that when using “local” you also need
  to set the `self_contained` option to false.

- Specify an alternate URL to load MathJax from another location.

- Specify null to exclude MathJax entirely.

For example, to use a local copy of MathJax:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    mathjax: local
    self_contained: false
---
```

To use a self-hosted copy of MathJax:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    mathjax: "http://example.com/mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
---
```

To exclude MathJax entirely:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    mathjax: null
---
```

## Document Dependencies

By default R Markdown produces standalone HTML files with no external
dependencies, using data: URIs to incorporate the contents of linked
scripts, stylesheets, images, and videos. This means you can share or
publish the file just like you share Office documents or PDFs. If you’d
rather keep dependencies in external files you can specify
`self_contained: false`. For example:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    self_contained: false
---
```

Note that even for self contained documents MathJax is still loaded
externally (this is necessary because of it’s size). If you want to
serve MathJax locally then you should specify `mathjax: local` and
`self_contained: false`.

One common reason keep dependencies external is for serving R Markdown
documents from a website (external dependencies can be cached separately
by browsers leading to faster page load times). In the case of serving
multiple R Markdown documents you may also want to consolidate dependent
library files (e.g. Bootstrap, MathJax, etc.) into a single directory
shared by multiple documents. You can use the `lib_dir` option to do
this, for example:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    self_contained: false
    lib_dir: libs
---
```

## Reveal Plugins

You can enable various reveal.js plugins using the `reveal_plugins`
option. Plugins currently supported include:

| Plugin                                                                             | Description                                                                                                                           |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [notes](https://revealjs.com/speaker-view/)                                        | Present per-slide notes in a separate browser window. Open Note view pressing `S`.                                                    |
| [zoom](http://lab.hakim.se/zoom-js/)                                               | Zoom in and out of selected content with `Alt+Click.`                                                                                 |
| [search](https://github.com/hakimel/reveal.js/blob/master/plugin/search/search.js) | Find a text string anywhere in the slides and show the next occurrence to the user. Open search box using `CTRL + SHIFT + F`.         |
| [chalkboard](https://github.com/rajgoel/reveal.js-plugins/tree/master/chalkboard)  | Include handwritten notes within a presentation. Press `c` to write on slides, Press `b` to open a whiteboard or chalkboard to write. |
| [menu](https://github.com/denehyg/reveal.js-menu)                                  | Include a navigation menu within a presentation. Press `m` to open the menu.                                                          |

Note that the use of plugins requires that the `self_contained` option
be set to false. For example, this presentation includes both the
“notes” and “search” plugins:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    self_contained: false
    reveal_plugins: ["notes", "search"]
---
```

You can specify additional options for the `chalkboard` and `menu`
plugins using `reveal_options`, for example:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    self_contained: false
    reveal_plugins: ["chalkboard", "menu"]
    reveal_options:
      chalkboard:
        theme: whiteboard
        toggleNotesButton: false
      menu:
        side: right
---
```

No other plugins can be added in `revealjs_presentation()`. You can open
feature request for new plugins or you would need to use a custom
template to write your own HTML format including custom plugins.

## Advanced Customization

### Includes

You can do more advanced customization of output by including additional
HTML content or by replacing the core pandoc template entirely. To
include content in the document header or before/after the document body
you use the `includes` option as follows:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    includes:
      in_header: header.html
      before_body: doc_prefix.html
      after_body: doc_suffix.html
---
```

### Pandoc Arguments

If there are pandoc features you want to use that lack equivalents in
the YAML options described above you can still use them by passing
custom `pandoc_args`. For example:

``` yaml
---
title: "Habits"
output:
  revealjs::revealjs_presentation:
    pandoc_args: [
      "--title-prefix", "Foo",
      "--id-prefix", "Bar"
    ]
---
```

Documentation on all available pandoc arguments can be found in the
[pandoc user guide](https://pandoc.org/MANUAL.html#options).

## Shared Options

If you want to specify a set of default options to be shared by multiple
documents within a directory you can include a file named `_output.yaml`
within the directory. Note that no YAML delimiters or enclosing output
object are used in this file. For example:

**\_output.yaml**

``` yaml
revealjs::revealjs_presentation:
  theme: sky
  transition: fade
  highlight: pygments
```

All documents located in the same directory as `_output.yaml` will
inherit it’s options. Options defined explicitly within documents will
override those specified in the shared options file.

## Code of Conduct

Please note that the revealjs project is released with a [Contributor
Code of
Conduct](https://pkgs.rstudio.com/revealjs/CODE_OF_CONDUCT.html). By
contributing to this project, you agree to abide by its terms.
