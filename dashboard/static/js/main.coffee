$ ->
        reload = (state) ->
                if state is "LOAD"
                        location.reload(true)
                else
                        # refresh every hour
                        setTimeout(reload, 60*60*1000, "LOAD")

        # Doesn't matter what the first call is made with, so we use
        # "new"
        reload("NEW")