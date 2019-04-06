from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

url_list = {
    "ptt_movie": "https://www.ptt.cc/bbs/movie/index.html",
    "rent591": "https://www.591.com.tw/"
}

url = url_list["rent591"]

# Run chromedriver in background
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# browser = webdriver.Chrome(options=chrome_options, executable_path='./chromedriver')
browser = webdriver.Chrome(options=chrome_options)
# browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get(url)

# Wait for appearance of the element with class name 'area-box'
waitForIt = WebDriverWait(browser, 10).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, 'area-box'))
)

city_selection = browser.find_element_by_xpath('//*[@id="area-box-body"]/dl[1]/dd[2]')
click_city_selection = city_selection.click()

# Reload the page to refresh state of the browser
browser.get(url)

rent_tab = browser.find_element_by_xpath('/html/body/section[1]/div[3]/div/div[1]/a[3]')
click_rent_tab = rent_tab.click()

# Wait for appearance of the element with id 'container'
waitForIt = WebDriverWait(browser, 10).until(
    expected_conditions.presence_of_element_located((By.ID, 'container'))
)

# Location
city_selector = browser.find_element_by_xpath('//*[@id="search-location"]/span[1]')
click_city_selector = city_selector.click()
city_selector_2 = browser.find_element_by_xpath('//*[@id="optionBox"]/dl[1]/ul/li[2]/a')
click_city_selector_2 = city_selector_2.click()
country_selector = browser.find_element_by_xpath('//*[@id="optionBox"]/li[1]/label')
click_country_selector = country_selector.click()

# Type
type_selector = browser.find_element_by_xpath('//*[@id="search-kind"]/span[3]')
click_type_selector = type_selector.click()

# Price
lower_price_input = browser.find_element_by_xpath('//*[@id="rentPrice-min"]')
higher_price_input = browser.find_element_by_xpath('//*[@id="rentPrice-max"]')
lower_price_input.send_keys(5000)
higher_price_input.send_keys(10000)
price_selector = browser.find_element_by_xpath('//*[@id="search-price"]/sapn/input[3]')
click_price_selector = price_selector.click()

# Room
room_selector = browser.find_element_by_xpath('//*[@id="search-plain"]/span[1]')
click_room_selector = room_selector.click()

# Wait for the loading element disappear
try:
    waitForItOut = WebDriverWait(browser, 10).until_not(
        expected_conditions.invisibility_of_element_located((By.ID, 'j_loading'))
    )
except:
    pass

sleep(1)

soup = BeautifulSoup(browser.page_source, 'html.parser')
contents = soup.select('div#content ul')

# print(contents)

for i,content in enumerate(contents):
    link = content.select('li.infoContent h3 a')[0]
    price = content.select('div.price i')[0].get_text()
    print(i, link.get_text().strip())
    print('price:', price)
    print('link:', 'https:' + link['href'].strip())
    print('\n')
    
browser.quit()