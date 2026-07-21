from playwright.sync_api import sync_playwright, expect

def test_verify_test_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()


        page.goto("https://automationexercise.com")
        expect(page).to_have_title("Automation Exercise")
        page.get_by_role("button",name="Test Cases").click()
        expect(page.get_by_text("Below is the list of test Cases for you to practice the Automation. Click on the scenario for detailed Test Steps:")).to_be_visible()
        browser.close()

