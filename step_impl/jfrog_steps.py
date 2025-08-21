from getgauge.python import step, before_suite, after_suite
from playwright.sync_api import sync_playwright

playwright = None
browser = None
page = None

@before_suite
def before_suite():
    global playwright, browser, page
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

@after_suite
def after_suite():
    if page:
        page.close()
    if browser:
        browser.close()
    if playwright:
        playwright.stop()

@step("Navigate to JFrog website")
def navigate_to_jfrog():
    page.goto("https://jfrog.com/")

@step("Click on Book A Demo button")
def click_book_demo():
    page.click("text=Book A Demo")
    page.wait_for_load_state("networkidle")

@step("Take screenshot of the demo page")
def take_screenshot():
    page.screenshot(path="demo-page.png", full_page=True)
