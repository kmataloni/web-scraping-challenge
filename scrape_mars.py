from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager


# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)



def scrape_mars_news(browser):

    # Visit url
    url = "https://redplanetscience.com"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    mars_news_html = browser.html
    news_soup = BeautifulSoup(mars_news_html, "html.parser")

    # Get mars title
    news_title = news_soup.find('div', class_='content_title').text

    # Get mars paragraph
    news_paragraph = news_soup.find('div', class_='article_teaser_body').text


    # Close the browser after scraping
    browser.quit()

    # Return results
    return news_title, news_paragraph

def scrape_featured_image(browser):
    img_url_home = 'https://spaceimages-mars.com'
    browser.visit(img_url_home)

    full_image_url = browser.find_by_tag("button")[1]
    full_image_url.click()

    html = browser.html
    soup_JPL = BeautifulSoup(html, "html.parser")

    img_url = soup_JPL.find("img", class_="fancybox-image").get("src")
    
    featured_image_url = img_url_home + "/" + img_url
    
    return featured_image_url

# def scrape_mars_facts():
#     try:
#         marsDF = pd.read_html("https://galaxyfacts-mars.com/")[0] 
#     except BaseException:
#         return None
#     marsDF.drop(marsDF.columns[[2]], axis = 1, inplace = True)
#     marsDF.columns=["Metric", "Value"]
#     marsDF.set_index("Metric", inplace=True)

#     return marsDF.to_html(classes="table table-striped")

# def scrape_mars_hemispheres(browser):
#     # create base url 
#     hemisphere_base_url = "https://marshemispheres.com"

#     # use browser to vist page
#     browser.visit(hemisphere_base_url)

#     hemisphere_image_urls = []

#     # list of hemispheres
#     hemisphere_list = browser.find_by_css("a.product-item h3")


#     # iterate through each url
#     for i in range(len(hemisphere_list)):
#         # create empty dictionary
#         hemisphere_dict = {}
        
        
#         # click through to hemisphere i
#         browser.find_by_css("a.product-item h3")[i].click()
        
        
#         # get image hrefs find by text (sample)
#         sample = browser.find_by_text("Sample").first
        
        
#         hemisphere_dict["img_url"] = sample["href"]
        
#         # get image by title
        
#         hemisphere_dict["title"] = browser.find_by_css("h2.title").text
        
#         hemisphere_image_urls.append(hemisphere_dict)
        
#         # go back to home page
#         browser.back()
#     return hemisphere_image_urls

def scrape_all_pages():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = scrape_mars_news(browser)
    # featured_image_url = scrape_featured_image(browser)
    # facts = scrape_mars_facts()
    # hemisphere_image_urls = scrape_mars_hemispheres(browser)

    
    
    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        # "featured_img": featured_image_url,
        # "facts": facts,
        # "hemispheres": hemisphere_image_urls,

    }
    #browser.quit()
    return mars_data
