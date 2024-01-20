from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 

options = Options()
options.page_load_strategy = 'eager'

driver = webdriver.Firefox(options=options)
URL = "https://www.imdb.com/title/tt7984734/"
TECH_URL = URL + "?ref_=tt_spec_sm"

print(TECH_URL)

#driver.get(URL)

# get images
#images = driver.find_elements(By.CLASS, "ipc-photo")


driver.get(URL)

images = driver.find_elements(By.CLASS_NAME, 'ipc-lockup-overlay')

print(len(images))

image_links = []

for img in images:
    link = img.get_attribute('href')
    if link and 'mediaviewer' in link:
        image_links.append(link)
    #print(img)
    #print(img.get_attribute('class'))
    print(link)
    print("---------")

#for img in images:
#    href = img.find_element(By.XPATH, "//a[@href]")
#    print(img.get_attribute('class'), href.get_attribute('href'))

'''
tech = driver.find_element(By.XPATH, '//section[data-cel-widget="StaticFeature_TechSpecs"]') 
print(tech)

color = driver.find_element(By.ID, "colorations")

print(color)
print("----------")
print(color.text)
'''

