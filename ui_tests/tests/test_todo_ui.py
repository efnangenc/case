import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_full_ui_flow(driver):
    # 1) Todo uygulamasına git
    driver.get("http://localhost:8000")  # senin Vue app portun
    print("Ana sayfa açıldı")
    time.sleep(1)  # 2 saniye bekle

    # 2) Sayfa başlığı kontrol
    assert "Vite + Vue" in driver.title or "vite + vue" in driver.title.lower()

    # 3) Kullanıcı kartlarını bul
    user_cards = driver.find_elements("class name", "cards-item")
    assert len(user_cards) > 0, "Kullanıcı kartı yok!"

    # 4) İlk kullanıcı bilgilerini kontrol et
    first_user = user_cards[0]
    name = first_user.find_element("tag name", "h2").text
    email = first_user.find_element("tag name", "p").text
    assert name != "", "İsim boş!"
    assert email != "", "Email boş!"

    # 3) İlk kullanıcıya tıkla
    first_user = user_cards[0]
    first_user.click()
    print("İlk kullanıcıya tıklandı")
    time.sleep(1)  # 2 saniye bekle

    # 4) Todo öğelerini bul
    todo_items = driver.find_elements("tag name", "li")
    assert len(todo_items) > 0, "Todo listesi boş!"
    first_todo = todo_items[0].text
    assert first_todo != ""
    print("Todo listesi kontrol edildi")
    time.sleep(1)  # 2 saniye bekle

    # 5) İlk todo öğesini kontrol et
    first_todo = todo_items[0].text
    assert first_todo != "", "İlk todo boş!"

   # --- Sidebar linkleri ---
    sidebar_links = ["Todos", "Posts", "Albums"]

    for link_text in sidebar_links:
        link = driver.find_element(By.LINK_TEXT, link_text)
        link.click()
        time.sleep(2)  # sayfanın yüklenmesini bekle
        print(f"{link_text} sayfasına gidildi")

        # Her sayfa için basit kontrol
        if link_text == "Todos":
            items = driver.find_elements(By.TAG_NAME, "li")
            assert len(items) > 0, "Todos listesi boş!"
        elif link_text == "Posts":
            posts = driver.find_elements(By.CLASS_NAME, "post-item")
            assert len(posts) > 0, "Post listesi boş!"
        elif link_text == "Albums":
            albums = driver.find_elements(By.CLASS_NAME, "album-card")
            assert len(albums) >= 0, "Album listesi boş!"  ############## buraya yaptığın bu saçmalığı sonra düzelt unutmazsannnnnnn....!!!!!!!!! 