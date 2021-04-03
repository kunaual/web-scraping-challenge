# web-scraping-challenge
jupyter notebook, MongoDB and Flask Application

Project goals are to scrape a few mars science new sites for text, images and table data. Store date in mongoDB, and create a summary html page to display the scraped data.


Files in this repo:
    * templates/index.html - html page utilizing some bootstrap basics and jinja to display scraped data

    * appy.py - uses flask, mongodb, and imported scrap mars functions.
    * mars_earth_comp.html - temp data file used to display table of mars-earth comparison info output from to_html command
    * mars_facts.html - temp data file used to display table output from to_html command
    * mission_to_mars.ipynb - jupyter notebook used to workout necessary scraping code.
    * scrape_mars.py - uses splinter, beautiful soup, chromedrivermanager, and pandas to perform scrapes to obtain article data, featured image, hemispheres list of images, and a mars facts table



