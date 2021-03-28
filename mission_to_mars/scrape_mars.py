from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

#uses sprinter to createa a browser.   browser goes to the test site
#scraps it 
#this is homework similar
#**<thing> is kwarg key word argument
def scrape():
    ''' scrapes page and inserts into db and then returns to index'''
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
	
	big_dict = {}
	url = 'https://redplanetscience.com/'
	browser.visit(url)

    html = browser.html  #get all the html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('div', class_='content_title').text
    teaser_text = soup.find('div', class_='article_teaser_body').text
    print(teaser_text)

    # Quit the browser
    browser.quit()

    return listings
