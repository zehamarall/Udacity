import webbrowser


class Movie ():
    """ Contructor of Class Movie

        Attributes:
            title (str): String movie title
            storyline (str): String movie story line of filme
            poster_image_url (str): Url from image poster
            trailer_youtube_url (str): Url from youtube trailer

    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                         trailer_youtube):
        # Constructor of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Method  show trailer on webbrowser
        webbrowser.open(self.trailer_youtube_url)
