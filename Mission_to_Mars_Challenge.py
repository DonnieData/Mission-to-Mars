#!/usr/bin/env python
# coding: utf-8

# In[37]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import time


# In[13]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)


# ### Visit the NASA Mars News Site

# In[14]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[15]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[16]:


slide_elem.find("div", class_='content_title')


# In[17]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[18]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# In[19]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[20]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[21]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[22]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[23]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[24]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ### Mars Facts

# In[25]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[26]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[27]:


df.to_html()


# ### Mars Weather

# In[28]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[29]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[30]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[47]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[48]:


# 2. Create a list to hold the images and titles.
hemispheres_info = []
base_url = 'https://astrogeology.usgs.gov'

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# parse site
html = browser.html
html_soup = soup(html, 'html.parser')
# drill down with html tags that contain desired data 
mars_info_container = html_soup.select('div.description')


# loop through scraped data, scrape additonal data and format 
for i in list(range(len(mars_info_container))):
        
    # parse extracted data and retrieve article header 
    header = mars_info_container[i].find('h3').get_text()
    
    # retrieve embedded parital url and convert to full webpage link
    article_partial_url = mars_info_container[i].find('a').get('href')
    article_full_url = f'{base_url}{article_partial_url}'
    
    # visit article site 
    browser.visit(article_full_url)
    html = browser.html
    #parse page 
    image_parse = soup(html, 'html.parser')
    
    #retreive full-resolution image image url via tags
    image_url = image_parse.select_one('ul li a').get('href')
    
    #format data into dictionary 
    hemispheres_info.append({'img_url':image_url,'title':header})
    time.sleep(.04)


# In[49]:


# 4. Print the list that holds the dictionary of each image url and title.
hemispheres_info


# In[50]:


# 5. Quit the browser
browser.quit()


# In[ ]:




