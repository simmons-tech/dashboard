$ ->
         $.get('/events', (events) ->
                addEvent = (data) ->
                        template = "<td> #{data.time} </td><td> #{data.title} </td>"
                        $('#events tbody tr').append(template)
                        
                for event in events
                        addEvent(event)
                )