from selenium import webdriver
import time
# Using Chrome to access web
url = input("Input exact path of the Chrome Driver : ")

while True:
    driver = webdriver.Chrome(executable_path=url)
    # Open the website
    driver.get('https://echo.msk.ru/polls/2720047-echo.html')

    id_box_select = driver.find_element_by_id('poll_a_200209')

    id_box_submit = driver.find_elements_by_name("submit")

    id_box_select.click()

    id_box_submit[3].click() 

    time.sleep(10)

    driver.close()

