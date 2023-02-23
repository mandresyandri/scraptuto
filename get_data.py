import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3

url = "https://agenda.meudon.fr"
response = requests.get(url)
driver = webdriver.Chrome(executable_path="/Users/mandresyandri/Desktop/scraptuto/chromedriver")

# Verify
if response.status_code != 200:
    print(f"Attention erreur \n {response.status_code}")
else:
    print("Go scrap !")

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button.rdrStaticRange:nth-of-type(3)"))
)
button_week_end = driver.find_element(By.CSS_SELECTOR, "button.rdrStaticRange:nth-of-type(3)")
button_week_end.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "title"))
)

titles = list()
for title in driver.find_elements(By.CSS_SELECTOR, "h1.title"):
    titles.append(title.text)

dates = list()
for date in driver.find_elements(By.CSS_SELECTOR, "div.media-body > div.detail-item:nth-of-type(1)"):
    dates.append(date.text)

lieux = list()
for lieu in driver.find_elements(By.CSS_SELECTOR, "div.media-body > div.detail-item:nth-of-type(2)"):
    lieux.append(lieu.text)

info_sup = list()
for info in driver.find_elements(By.CSS_SELECTOR, "div.media-body > div.detail-item:nth-of-type(3)"):
    info_sup.append(info.text)

def insert_data(i):
    scrapped_data = {
        "title" : titles[i],
        "date" : dates[i],
        "lieu" : lieux[i]
    }

    conn = sqlite3.connect("data-scrap.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO scraped_data(title, date, lieu) VALUES(:title, :date, :lieu)
    """, scrapped_data)
    conn.commit()

i = 0
while i < len(titles):
    insert_data(i)
    i += 1

driver.close()

print("Element was scraped and insert into DB")