import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from royale.pages.pages import Pages
from royale.services import card_service


@pytest.fixture
def royale():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')
    pages = Pages(driver)
    yield pages
    driver.quit()


api_cards = card_service.get_all_cards()


@pytest.mark.parametrize('api_card', api_cards)
def test_card_is_displayed(royale, api_card):
    royale.cards.goto()
    card = royale.cards.get_card_by_name(api_card.name)
    assert card.is_displayed


@pytest.mark.parametrize('api_card', api_cards)
def test_card_details_are_correct(royale, api_card):
    royale.cards.goto()
    royale.cards.get_card_by_name(api_card.name).click()

    royale.card_details.wait_for_page_load()
    card = royale.card_details.get_base_card()

    assert card.name == api_card.name
    assert card.type == api_card.type
    assert card.arena == api_card.arena
    assert card.rarity == api_card.rarity
