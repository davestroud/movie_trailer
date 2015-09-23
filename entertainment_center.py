import fresh_tomatoes

__author__ = 'davidstroud'

import media

god_father = media.Movie("The Godfather",
                         "A story of a mans live in la cosa nostra",
                         "https://c2.staticflickr.com/4/3646/3701323796_585f6b1719.jpg",
                         "https://youtu.be/sY1S34973zA")
casino = media.Movie("Casino",
                     "The story of the Las Vega Mafia",
                     "http://static.rogerebert.com/uploads/movie/movie_poster/casino-1995/large_6rRqNMDjYdJhtIgYSwiX91QgBTq.jpg",
                     "https://www.youtube.com/watch?v=ZN6mp2NjMhs")
the_departed = media.Movie("The Departed ",
                           "A rogue cop's undercover life in the Boston Mafia",
                           "http://static.rogerebert.com/uploads/movie/movie_poster/the-departed-2007/large_tGLO9zw5ZtCeyyEWgbYGgsFxC6i.jpg",
                           "https://www.youtube.com/watch?v=LfHZMMDGKJ0")
movies = [god_father,casino,the_departed]
fresh_tomatoes.open_movies_page(movies)




