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
	
    article_dict={}
    print('----------------------------------------------------------------------')
    print(soup.find('div', class_='content_title').get_text())
    print(soup.find('div', class_='article_teaser_body').get_text())
    title = soup.find('div', class_='content_title').get_text()
    teaser_text = soup.find('div', class_='article_teaser_body').get_text()
    article_dict['title']=title
    article_dict['teaser_text']=teaser_text
    print(teaser_text)

    
    # Quit the browser
    browser.quit()

    return article_dict
