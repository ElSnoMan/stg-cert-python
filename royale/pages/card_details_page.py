from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from royale.models.card import Card


class CardDetailsPage:
    def __init__(self, driver: WebDriver):
        self.map = CardDetailsPageMap(driver)
        self.wait = WebDriverWait(driver, 10)

    def get_base_card(self) -> Card:
        card_deets = self.map.card_deets.text.split(', ')
        card_type = card_deets[0]  # "Troop"
        card_arena = int(card_deets[1].split()[-1])  # "Arena 8"
        card_name = self.map.card_name.text
        card_rarity = self.map.card_rarity.text

        card = {
            'id': 0,
            'cost': 0,
            'icon': None,
            'name': card_name,
            'rarity': card_rarity,
            'type': card_type,
            'arena': card_arena
        }

        return Card(**card)

    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Statistics']")))


class CardDetailsPageMap:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def card_name(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='cardName']")

    @property
    def card_deets(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[class='card__rarity']")

    @property
    def card_rarity(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='card__count']")
