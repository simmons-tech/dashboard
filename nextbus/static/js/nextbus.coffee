$ ->
        getNextbus = ->
                $.get('/nextbus', (bus) -> 
                        # title not used in current dashboard
                        $("#nextbus .title").html(bus.title)
                        $("#nextbus .next").html("#{bus.next} min")
                        $("#nextbus .second").html("#{bus.second} min")
                        $("#nextbus .third").html("#{bus.third} min")
                )

                # Update every 15 seconds
                setTimeout(getNextbus, 15000)

         getNextbus()
