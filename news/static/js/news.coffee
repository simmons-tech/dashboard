$ ->
        getNews = ->
                $.get('/news', (news) ->
                        $('#news .title').html(news.title)
                )

                setTimeout(getNews, 10000)

        getNews()