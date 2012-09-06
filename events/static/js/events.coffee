$ ->
        getEvent = ->
                $.get('/events', (event) ->
                        $('#events .title').html(event.title)
                        $('#events .time').html(event.time)
                )

                setTimeout(getEvent, 15000)

        getEvent()
                