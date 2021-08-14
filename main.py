from selenium import webdriver
import time

chrome_driver_path = "/Development/chromedriver.exe"
GAME_URL = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(GAME_URL)

game_is_on = True
timeout = time.time() + 5*60  # 5 minutes

cookie = driver.find_element_by_css_selector("#cookie")


def clicking():
    click_timeout = time.time() + 5
    while time.time() < click_timeout:  # loop ends after 5s
        cookie.click()


def buy():
    store_items = [
        driver.find_element_by_css_selector("#buyCursor b"),
        driver.find_element_by_css_selector("#buyGrandma b"),
        driver.find_element_by_css_selector("#buyFactory b"),
        driver.find_element_by_css_selector("#buyMine b"),
        driver.find_element_by_css_selector("#buyShipment b"),
        driver.find_element_by_xpath("//*[@id='buyAlchemy lab']/b"),
        driver.find_element_by_css_selector("#buyPortal b"),
        driver.find_element_by_xpath("//*[@id='buyTime machine']/b"),
    ]

    money = int(driver.find_element_by_css_selector("#money").text.replace(",", ""))
    store_items_cost = [int(item.text.split("-")[1].strip().replace(",", "")) for item in store_items]

    for item_cost in store_items_cost:
        if money < item_cost:
            index = store_items_cost.index(item_cost) - 1
            store_items[index].click()
            break


while game_is_on:
    clicking()
    print("clicking over")
    buy()
    if time.time() > timeout:
        game_is_on = False
        cookies_seconds = driver.find_element_by_css_selector("#cps").text
        print(cookies_seconds)


driver.close()


