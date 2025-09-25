from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)

       
        login_page.goto(os.getenv("LOGIN_URL")) 


        login_page.login(os.getenv("LOGIN_EMAIL"), os.getenv("LOGIN_PASSWORD"))

        
        page.wait_for_selector("text=Connecté(e).")  

        print("✅ Message 'Connecté(e).' trouvé")

        browser.close()
