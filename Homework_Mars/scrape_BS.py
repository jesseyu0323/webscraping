from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

def scrape(): 
url1 = 'https://mars.nasa.gov/news/'.text
url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'.text
url3 = 'https://twitter.com/marswxreport?lang=en'.text
url4 = 'http://space-facts.com/mars/'
url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'.text


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

mars_collection = {}

soup = BeautifulSoup(url1, 'lxml')
news_title = soup.select_one(".content_title").get_text(strip=True)
news_p = soup.select_one(".rollover_description_inner").get_text(strip=True)
mars_collection['news_title'] = news_title
mars_collection['news_p'] = news_p

soup = BeautifulSoup(url2, 'lxml')
image_url = soup.select_one(".carousel_item")['style']
strip = re.findall("url\('(.*?)'\)", image_url)[0]
featured_image_url = "https://www.jpl.nasa.gov/" + feature_Image
mars_collection['featured_image_url'] = featured_image_url

soup = BeautifulSoup(url3, 'lxml')
tweets = soup.find_all("p", class_="tweet-text")
for tweet in tweets:
    if tweet.text.partition(' ')[0] == 'Sol':
        mars_weather = tweet.text
        break
mars_collection['mars_weather'] = mars_weather

mars_facts_df = pd.read_html(url4, attrs={'id': 'tablepress-mars'})[0]
mars_facts_df = mars_facts_df.set_index(0).rename(columns={1: "value"})
del mars_facts_df.index.name
mars_facts = mars_facts_df.to_html(justify='left')
mars_collection['mars_facts'] = mars_facts

soup = BeautifulSoup(url5, 'lxml')
title = soup.find_all('h3')

def hemisphere_images():
    one_image = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    two_image = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    three_image = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    four_image = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    full_hemisphere_dict = {"one_image": one_image, "two_image":two_image, "three_image":three_image, "four_image":four_image}

    return full_hemisphere_dict