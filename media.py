import webbrowser


# define and initialize class Movie.
# Constructor is called and self is initialized.
class Movie:
    """Return the pathname of the Movie root directory."""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # create instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # create instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
