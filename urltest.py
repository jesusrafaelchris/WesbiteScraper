from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random_words import RandomWords
import time
rw = RandomWords()

word1 = rw.random_word()
word2 = rw.random_word()
search_query = str(word1) + '+' + str(word2)
print(search_query)

driver = "/Users/christiangrinling/Downloads/chromedriver"
browser = webdriver.Chrome(driver)

browser.get("https://www.inboxdollars.com/")
print("Current Page Title is : %s" %browser.title)

first_login = '//*[@id="log-me"]/a'

login_name = '//*[@id="loginname"]'

login_password = '//*[@id="pwd"]'

login_submit = '//*[@id="loginForm"]/div[4]/div/input'

browser.find_element_by_xpath(first_login).click()
browser.find_element_by_xpath(login_name).send_keys("grinlingc@gmail.com")
browser.find_element_by_xpath(login_password).send_keys("q$VXKu*_vY9!k.P")
browser.find_element_by_xpath(login_submit).click()

time.sleep(5)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[1])
browser.get("https://www.inboxdollars.com/search/infospace?query=" + search_query + "&category=web&x=0&y=0")
time.sleep(3)
