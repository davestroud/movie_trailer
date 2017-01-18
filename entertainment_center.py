import fresh_tomatoes
import media
# create  and define instances of the class movie to build the objects.
# used url shortener to shorten youtube links
god_father = media.Movie("The Godfather",
                         "A story of a mans life in la cosa nostra",
                         "https://goo.gl/2PMXIH",
                         "https://youtu.be/sY1S34973zA")
casino = media.Movie("Casino",
                     "The story of the Las Vega Mafia",
                     "https://goo.gl/043Mbq",
                     "https://youtu.be/-L5Zx34mjUU")
the_departed = media.Movie("The Departed ",
                           "A rogue cop's undercover life in the Boston Mafia",
                           "https://goo.gl/G2ALDY",
                           "https://youtu.be/iQpb1LoeVUc")
# define array of movies
movies = [god_father, casino, the_departed]
# calls the function open_movies_page
fresh_tomatoes.open_movies_page(movies)
