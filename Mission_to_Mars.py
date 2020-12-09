# import libraries 
from splinter import Browser 
from bs4 import BeautifulSoup as soup
import pandas as pd

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path':'chromedriver.exe'}
browser = Browser('chrome', **executable_path)

# Visit the mars nasa news site
# tell splinter to  visit the qoutes to scrape site 
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page ( to respect terms of service and site servers)
# searching for specific combination of tags and attributes ex -- ul.item_list
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# html parser 
# parse all of the html of the page with beautiful soup
html = browser.html
news_soup = soup(html, 'html.parser')
# "."" is used for selecting classes, pinpoints the <li /> tag with the class of slide and the <ul /> tag with a class of item_list.
# will select last item 
slide_elem = news_soup.select_one('ul.item_list li.slide')

# look inside of slide_elem for data within div tag that hass cotent_title as class
slide_elem.find("div", class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# Visit the webpage.
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# # Find and click the "full image" button # using the unique "id=full_image"
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# Find the "more info" button and click 
# button doesnt have any unique identifiers ( eg. class or id), so searching for it by text
# checks if element is present and returns bool 
browser.is_element_not_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()

# Parse the resulting html with soup 
html = browser.html
img_soup = soup(html,'html.parser')

# pull the most recent image via tags and not direct image link (so that we get the updated image every time and not the specified same image)
# Find the relative image url
#Note src link is in double qoutes("") and not single('')

img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# image only uses partial link, which is its location within the site. to get full link simply append partial onto base link of site 
base_url = 'https://www.jpl.nasa.gov'
img_url = f'{base_url}{img_url_rel}'
img_url

# read html page with pandas
#pandas specifically searches for and returns a list of tables found
df = pd.read_html('https://space-facts.com/mars/')[0]
df.head()

# rename columns 
df.columns=['description', 'value']
# set description column as index 
df.set_index('description', inplace=True)
df

# convert extracted table to html so it can be displayed in web app/webpage
df.to_html()

# close automated browser session
browser.quit()