# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
import os
from dotenv import load_dotenv

load_dotenv()

IG_LOGIN = os.getenv('IG_LOGIN')
IG_PASS = os.getenv('IG_PASS')


class InstaFollower:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()

    def login(self):
        self.driver.get('https://www.instagram.com/')

        # Insert username
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.NAME, 'username')
        )).send_keys(IG_LOGIN)

        # Insert password
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.NAME, 'password')
        )).send_keys(IG_PASS)

        # Click login button
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        )).click()

    def find_followers(self, username):
        # Open the Followers modal
        self.driver.get(f'https://www.instagram.com/{username}')
        target_href = f'/{username}/followers/'
        xpath_expression = f'//a[@href="{target_href}"]'
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, xpath_expression)
        )).click()

    def scroll_down(self):
        # Scroll down in the Followers modal
        popup_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        ))
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup_element)

    def follow(self):

        # Follow each account in the Followers modal
        try:
            follow_buttons = self.driver.find_elements(By.XPATH,'//div[@class="_aano"]//button[contains(@class, "_acan") and .//div[text()="Follow"]]')

            for button in follow_buttons:
                button.click()
                time.sleep(1)

        except ElementClickInterceptedException as e:
            print(e)
            pass
