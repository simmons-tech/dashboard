$ ->
        getWeather = ->
                $.get('/weather', (data) ->
                        current = data.current
                        today = data.today
                        tomorrow = data.tomorrow

                        # Current Weather
                        $('#current .temp').html("#{current.temp}&deg;F")
                        $('#current .description').html(current.description)

                        forecast = (data, id) ->
                                for key,value of data
                                        param = "##{id} .#{key}"
                                        $(param).html(value)

                        forecast(today, 'today')
                        forecast(tomorrow, 'tomorrow')
                        )

                # Update every 2 minutes
                setTimeout(getWeather, 120000)

        getWeather()
                