$ ->
        next = (show) ->
                show.next()

                setTimeout(next, 5000, slideshow)

        slideshow = new SlideShow(queryAll('.slide'))
        next(slideshow)
        
                