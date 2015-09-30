import fresh_tomatoes
import media
# create  and define instances of the class movie to build the objects.
# used url shortener to shorten youtube links
god_father = media.Movie("The Godfather",
                         "A story of a mans live in la cosa nostra",
                         "https://goo.gl/Ad6SvC",
                         "https://youtu.be/sY1S34973zA")
casino = media.Movie("Casino",
                     "The story of the Las Vega Mafia",
                     "http://goo.gl/QJnBoz",
                     "https://youtu.be/-L5Zx34mjUU")
the_departed = media.Movie("The Departed ",
                           "A rogue cop's undercover life in the Boston Mafia",
                           "http://goo.gl/ClJt3o",
                           "https://youtu.be/iQpb1LoeVUc")
# define array of movies
movies = [god_father, casino, the_departed]
# calls the function open_movies_page
fresh_tomatoes.open_movies_page(movies)
