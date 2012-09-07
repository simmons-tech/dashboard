$ ->
        getTime = ->
                d = new Date()
                h = d.getHours()
                m = d.getMinutes();

                # 12 hour clock
                if h > 12
                        h -= 12

                # two digit minute
                if m < 10
                        m = "0#{m}"

                $('#time h1').html("#{h}:#{m}")

                # day of week
                dow = d.getDay()

                days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

                dow = days[dow]

                dom = d.getDate()

                month = d.getMonth()

                months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

                month = months[month]

                $('#time h2').html("#{dow}, #{month} #{dom}")

                setTimeout(getTime, 5000)

        getTime()
        