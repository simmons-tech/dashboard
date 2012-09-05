$ ->
         $.get('/events', (events) ->
                addEvent = (data) ->
                        $('#events .title').html(data.title)
                        $('#events .time').html(data.time)
                        
                for event in events
                        addEvent(event)
                )