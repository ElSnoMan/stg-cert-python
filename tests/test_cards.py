import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from royale.pages.pages import Pages


@pytest.fixture
def royale():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')
    pages = Pages(driver)
    yield pages
    driver.quit()


card_names = ['Ice Spirit', 'Mirror', 'Lava Hound']


@pytest.mark.parametrize('card_name', card_names)
def test_card_is_displayed(royale, card_name):
    royale.cards.goto()
    card = royale.cards.get_card_by_name(card_name)
    assert card.is_displayed


def test_ice_spirit_details_are_correct(royale):
    # 1. go to statsroyale
    # 2. open cards page
    # 3. go to Ice Spirit's Details Page
    # 4 assert name, type, arena, and rarity are correct

    cards_link = royale.find_element(By.CSS_SELECTOR, "a[href='/cards']")
    cards_link.click()

    ice_spirit = royale.find_element(By.CSS_SELECTOR, "a[href*='Ice+Spirit']")
    ice_spirit.click()

    card_name = royale.find_element(By.CSS_SELECTOR, "[class*='cardName']").text
    # text in element is "Troop, Arena 8"
    card_deets = royale.find_element(By.CSS_SELECTOR, "[class='card__rarity']").text.split(', ')
    # after splitting we get ["Troop", "Arena 8"] so we can assign type and arena
    card_type = card_deets[0]
    card_arena = card_deets[1]
    card_rarity = royale.find_element(By.CSS_SELECTOR, "[class*='card__count']").text

    assert card_name == 'Ice Spirit'
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'
    assert card_rarity == 'Common'
