# import libraries 
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }
    # Stop webdriver and return data
    browser.quit()
    return data


# browser varaible as arguemnt needed to automate 
def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # searching for specific combination of tags and attributes ex -- ul.item_list
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # parse all of the html of the page with beautiful soup
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        # look inside of slide_elem for data within div tag that hass cotent_title as class
        slide_elem.find("div", class_='content_title')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()

    # handles errors that may occur froms craping      
    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser): 
    # Visit the webpage.
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # # Find and click the "full image" button # using the unique "id=full_image"
    full_image_elem = browser.find_by_id('full_image')[0]
    full_image_elem.click()

    # Find the "more info" button and click 
    browser.is_element_not_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup 
    html = browser.html
    img_soup = soup(html,'html.parser')

    try: 
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")

    except AttributeError:
        return None

    # image only uses partial link, which is its location within the site. 
    base_url = 'https://www.jpl.nasa.gov'
    img_url = f'{base_url}{img_url_rel}'

    return img_url

def mars_facts():
    try:    
        # read html page with pandas
        df = pd.read_html('https://space-facts.com/mars/')[0]
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['description', 'value'] 
    df.set_index('description', inplace=True)

    # convert extracted table to html so it can be displayed in web app/webpage
    return df.to_html(classes="table table-striped")

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())