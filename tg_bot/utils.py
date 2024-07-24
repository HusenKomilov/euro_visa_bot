from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

url = os.getenv("url")
login = os.getenv("login")
password = os.getenv("password")


def main():
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()))

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 5)

        x = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#menuArea > span:nth-child(2)")))
        x.click()
        driver.switch_to.frame("mainWindow")
        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "j_username")))
        username_field.send_keys(login)
        password_field = wait.until(
            EC.presence_of_element_located((By.ID, "j_password")))
        password_field.send_keys(password)

        login_btn = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#infoBarBigInnerDiv > table > tbody > tr:nth-child(4) > td > font")))
        login_btn.click()
        zbz = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "#infoBarInnerDiv > table > tbody > tr:nth-child(2) > td > a"
        )))
        zbz.click()
        choices = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "#calendar\.consularPost\.consularPost"
        )))
        choices.click()
        options = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "#calendar\.consularPost\.consularPost > option:nth-child(60)"
        )))
        options.click()
        option_btn = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "#infoBarInnerDiv > table > tbody > tr:nth-child(3) > td:nth-child(2) > font"
        )))
        option_btn.click()

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        tbody = soup.select("#infoBarBigInnerDiv > table > tbody")
        spaces = {}

        for i in tbody:
            for j in i.find_all("td", class_="calendarMonthCell"):
                x = j.find_all("font", class_="pointer")
                if x is not None:
                    for asd in x:
                        z = asd.text.strip()
                        xas = z[8:].replace("[", "")
                        xas = xas.replace("]", "")
                        if int(xas.split("/")[1]) > int(xas.split("/")[0]):
                            spaces[z[0:5]] = xas
                        else:
                            pass

                else:
                    pass
        if len(spaces.keys()) == 0:
            next_month = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nextMonthLabel")))
            next_month.click()
            for i in tbody:
                for j in i.find_all("td", class_="calendarMonthCell"):
                    x = j.find_all("font", class_="pointer")
                    if x is not None:
                        for asd in x:
                            z = asd.text.strip()
                            xas = z[8:].replace("[", "")
                            xas = xas.replace("]", "")
                            if int(xas.split("/")[1]) > int(xas.split("/")[0]):
                                spaces[z[0:5]] = xas
                            else:
                                pass
                    else:
                        pass
        return spaces
    finally:
        pass
