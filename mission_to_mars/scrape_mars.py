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
	
    # get article info
    print('-----article code------------------------------------------------------------')
    print(soup.find('div', class_='content_title').get_text())
    print(soup.find('div', class_='article_teaser_body').get_text())
    title = soup.find('div', class_='content_title').get_text()
    teaser_text = soup.find('div', class_='article_teaser_body').get_text()
    big_dict['title']=title
    big_dict['teaser_text']=teaser_text
    
    # get featured image url
    iurl = 'https://spaceimages-mars.com/'
    browser.visit(iurl)
    print('-----featured image code------------------------------------------------------------')
    ihtml = browser.html
    isoup = BeautifulSoup(ihtml, 'html.parser')
    img = isoup.find('img', class_="headerimage")
    print(img)
    #concat the url to the image location
    featured_image_url = iurl+img['src']
    print(featured_image_url)

    big_dict['featured_image_url'] = featured_image_url

    #get hemispheres
    hurl = 'https://marshemispheres.com/'
    browser.visit(hurl)
    hemisphere_image_urls = []
    print('-----hemisphere code------------------------------------------------------------')
    html = browser.html  #get all the html
    hsoup = BeautifulSoup(html, 'html.parser')

    #get the list of 4 headers from main page and then loop through each.
    list_of_subpages = []
    a_itemlinks = hsoup.find_all('a', class_='itemLink')
    
    for alink in a_itemlinks:
        #print(alink['href']) #testing output
        cur_href = alink['href']
        if 'html' in cur_href:
            #print('it does') #testing output
            if cur_href not in list_of_subpages:
                #print('add it!') #testing output
                list_of_subpages.append(cur_href)

    print(list_of_subpages)


    for page in list_of_subpages:
        sub_url=hurl+page
        print(sub_url) #testing output
        
        browser.visit(sub_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup.prettify()) #testing output
        #looking for this <img class="wide-image" src="images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"/>
        img = soup.find('img', class_='wide-image')
        #print(img)
        #print(hurl+img['src'])
        title=soup.find('h2', class_='title').get_text()#.split(" Enhanced")[0]  #don't need to removed the word enhanced
        #print("title "+title)
        print(hurl+img['src'])  #testing output
        hemis_dict = {}
        hemis_dict['title'] = title
        hemis_dict['img_url'] = hurl+img['src']
        #print(hemis_dict)  #testing output
        hemisphere_image_urls.append(hemis_dict)


    big_dict['hemisphere_image_urls'] = hemisphere_image_urls
                







    
    # Quit the browser
    browser.quit()

    return big_dict
