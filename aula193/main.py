# type: ignore
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# from time import sleep


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent
# Caminho para a pasta onde o choromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH)
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # Exemple
    # options = '--headless',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com.br/')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Hello Word')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    links = browser.find_elements(By.TAG_NAME, 'a')
    links[0].click()

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)
