import webbrowser

class Movie(object):
   
    def __init__(run, movie_title, poster_image,
                 trailer_youtube):
        run.title = movie_title
        run.poster_image_url = poster_image
        run.trailer_youtube_url = trailer_youtube
       

    def show_trailer(run):
        webbrowser.open(run.trailer_youtube_url)
