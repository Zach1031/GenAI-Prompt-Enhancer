from bs4 import BeautifulSoup 

from imdb import Cinemagoer

import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 

import string

def search_movie(movie_title: str):
    imdb = Cinemagoer()

    movie = imdb.search_movie(movie_title)[0]
    movieID, movie_name = movie.movieID, movie['long imdb title']
 
    # IMDB url is straightforward
    imdb_URL = f"https://www.imdb.com/title/tt{movieID}/"


    # shot on what is the movie name, all lowercase, no punction, seperated by dashes, plus year number
    remove_chars = str.maketrans("", "", string.punctuation)
    formatted_name = '-'.join((movie_name.lower().translate(remove_chars).split(' ')))
    shot_on_what_URL = "https://shotonwhat.com/" + formatted_name

    #print(shot_on_what_URL)
    #print(scrape_specs(shot_on_what_URL))
    #print('============')

    #print(scrape_photos(imdb_URL))

# scrape camera specs and other related info
def scrape_specs(URL: str):
    # dictionary containing export values

    # page = requests.get(URL)

    # soup = BeautifulSoup(page.content, "html.parser")

    # local file used for testing
    local_file = open("lighthouse_camera.html")
    #soup = BeautifulSoup(requests.get(URL).content, "html.parser")
    soup = BeautifulSoup(local_file, "html.parser")

    export = {}

    # items are stored in singletablesw class
    tables = soup.find_all("div", {"class": "singletablesw"})

    left, right = tables[0], tables[1]

    # store camera model and genre based on position
    export['camera_model'], export['genres'], export['acquisition'] = left.find_all("div")[3].text, left.find_all("b")[0].text, left.find_all("div")[1].text

    right_divs = right.find_all("div")
    export['film_stock'], export['film_width'] = right_divs[9].text, right_divs[11].text 

    export['director'] = soup.find_all("div", {"class": "creatives"})[1].find_all("a")[0].text

    title = soup.find_all("div", {"class": "title_meta"})[0].find_all("a")
    for data in title:
        if 'distributed-aspect-ratio' in data['href']:
            export['aspect-ratio'] = data.text
        
        if 'color-profile' in data['href']:
            export['color'] = data.text


    return export

# scrape photos from imdb
def scrape_photos(URL: str):
    options = Options()
    options.page_load_strategy = 'eager'

    driver = webdriver.Firefox(options=options)
    driver.get(URL)

    images = driver.find_elements(By.CLASS_NAME, 'ipc-lockup-overlay')

    print(len(images))

    image_links = []

    for img in images:
        link = img.get_attribute('href')
        if link and 'mediaviewer' in link:
            image_links.append(link)

    return image_links

movie_name = input("enter movie name: ")
search_movie(movie_name)
