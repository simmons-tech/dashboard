$.get('/nextbus', (bus) -> 
        # title not used in current dashboard
        $("#nextbus .title").html(bus.title)
        $("#nextbus .next").html(bus.next)
        $("#nextbus .second").html(bus.second)
        $("#nextbus .third").html(bus.third)
        )

