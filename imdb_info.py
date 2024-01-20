# importing the module
from imdb import Cinemagoer
# creating an instance of the IMDB()
ia = Cinemagoer()
# Using the Search movie method
items = ia.search_movie('Avengers')

movie = items[0]
print(movie, movie['directors'])
