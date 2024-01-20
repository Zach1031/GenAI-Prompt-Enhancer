import requests
from bs4 import BeautifulSoup 

URL = ""

# page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")

# local file used for testing
local_file = open("lighthouse_camera.html")
soup = BeautifulSoup(local_file, "html.parser")

# items are stored in singletablesw class
test = soup.find_all("div", {"class": "singletablesw"})


left, right = test[0], test[1]

# store camera model and genre based on position
camera_model, genres, acquisition = left.find_all("div")[3].text, left.find_all("b")[0].text, left.find_all("div")[1].text

right_divs = right.find_all("div")
film_stock, film_width = right_divs[9].text, right_divs[11].text 

print(f"camera model: {camera_model}\ngenres: {genres}\nfilm stock: {film_stock}\nfilm width: {film_width}\nacquisition: {acquisition}")

director = soup.find_all("div", {"class": "creatives"})[1].find_all("a")[0].text
print(f"director: {director}")

