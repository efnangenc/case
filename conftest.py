import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Chrome'u aç
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Test bitince kapat
    driver.quit()
