from imdb import Cinemagoer
from bs4 import BeautifulSoup 


ia = Cinemagoer()
# Using the Search movie method
#items = ia.search_movie('Avengers')

#first_result = items[0]
#movie_ID = first_result.movieID

'''
movie = imdb.get_movie('000000')

print(sorted(movie.keys()))

local_file = open("lighthouse_imdb.html")
soup = BeautifulSoup(local_file, "html.parser")

for chunk in soup:
    print(chunk)

#ipc-photo: sample images
test = soup.find_all("div", {"class: ipc-photo"})
for result in test:
    print(result)
    '''

movie = ia.get_movie('7984734')

print(sorted(movie.keys()))
print(movie['color info'])

# sample URL
# https://www.imdb.com/title/tt7984734/
