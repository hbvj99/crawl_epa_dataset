from selenium import webdriver # import libraries
import csv

# d_location = []
d_url = [] # empty list
d_name = []

browser = webdriver.Chrome() # browser webdriver
browser.get('https://cfpub.epa.gov/airnow/index.cfm?action=airnow.global_summary#Nepal$Embassy_Kathmandu') #main url

element = browser.find_element_by_css_selector("#root > div > div > div:nth-child(1) > div:nth-child(2) > div > div > div > nav > ul > li:nth-child(3) > a").click() # click historical data

panelHeader =  browser.find_element_by_css_selector('.panelHeader') # select xpath

url = panelHeader.find_elements_by_tag_name('a') # tag name

span = panelHeader.find_elements_by_tag_name('span')

# location =  browser.find_element_by_css_selector("#root > div > div > div:nth-child(1) > div:nth-child(1) > div > div.col-xs-4 > div.aboutWrapper > h3")
# d_location.append(location.text)

# collect name, append to empty list
for name in span:
    url_name = name.text
    d_name.append(url_name)

# collect urls, append to list
for item in url:
    item_url = item.get_attribute('href')
    d_url.append(item_url)

browser.close() # browser exit

# write lists to csv file
with open('data/us_embassy_kathmandu.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(d_name, d_url))


