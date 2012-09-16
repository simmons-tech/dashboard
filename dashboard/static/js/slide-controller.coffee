$ ->
        next = (show) ->
                show.next()

                setTimeout(next, 15000, slideshow)

        slideshow = new SlideShow(queryAll('.slide'))
        next(slideshow)
        
                
