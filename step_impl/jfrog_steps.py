import os
from getgauge.python import step, before_suite, after_suite
from playwright.sync_api import sync_playwright

playwright = None
browser = None
page = None

@before_suite
def before_suite():
    global playwright, browser, page
    # Check if running in GitHub Actions
    is_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'
    
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=is_github_actions,  # headless in CI, headed locally
        args=['--start-maximized'] if not is_github_actions else None  # maximize window locally
    )
    
    # Set viewport size for consistent behavior
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080} if is_github_actions else None
    )
    page = context.new_page()

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
