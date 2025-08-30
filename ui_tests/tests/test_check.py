
# def test_open_google():
#     driver = webdriver.Chrome()
#     driver.get("https://www.google.com")
#     assert "Google" in driver.title
#     driver.quit()

def test_open_google(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title


# if __name__ == "__main__":
#     test_open_google()
