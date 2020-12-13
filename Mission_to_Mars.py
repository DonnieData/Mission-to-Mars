#!/usr/bin/env python
# coding: utf-8

# In[376]:


# import dependencies 
from splinter import Browser 
from bs4 import BeautifulSoup as soup

import pandas as pd
import time 


# In[198]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path':'chromedriver.exe'}
browser = Browser('chrome', **executable_path)


# In[380]:


# visit site
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# parse site
html = browser.html
html_soup = soup(html, 'html.parser')

# drill down with html tags that contain desired data 
mars_info_container = html_soup.select('div.description')
len(mars_info_container)
mars_info_container[0]


# In[397]:


mars_info_container[1].find('a')


# In[398]:


hemispheres_info = []
base_url = 'https://astrogeology.usgs.gov'


# In[399]:


# loop through scraped data, scrape additonal data and format 
for i in list(range(len(mars_info_container))):
    header = mars_info_container[i].find('h3').get_text()
    
    article_partial_url = mars_info_container[i].find('a').get('href')
    article_full_url = f'{base_url}{article_partial_url}'
    
    browser.visit(article_full_url)
    html = browser.html
    image_parse = soup(html, 'html.parser')
    
    image_url = image_parse.select_one('ul li a').get('href')
    
    #retrieve full-resolution title 
    hemispheres_info.append({'img_url':image_url,'title':header})
    time.sleep(.05)


# In[393]:


article_full_url


# In[400]:


# review 
hemispheres_info


# In[ ]:


# close scraping application 
browser.quit()


# -----

# In[ ]:





# In[ ]:





# In[ ]:




