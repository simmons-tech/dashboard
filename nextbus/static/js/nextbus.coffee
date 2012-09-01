$.get('/nextbus', (bus) -> 
        $("#nextbus .title").html(bus.title)
        $("#nextbus .next").html(bus.next)
        $("#nextbus .second").html(bus.second)
        $("#nextbus .third").html(bus.third)
        )

