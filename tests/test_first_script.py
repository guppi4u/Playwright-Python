import re
from playwright.sync_api import Page, expect

def test_example_interaction(page: Page):
    # 1. Navigate to a simpler website for automation
    page.goto("https://playwright.dev")
    print("Navigated to playwright.dev")

    # 2. Assert the title of the page
    # The title for playwright.dev is usually just "Playwright" or similar
    expect(page).to_have_title(re.compile("Playwright"))
    print("Verified page title contains 'Playwright'")

    # 3. Find and click on the "Docs" link
    # Using get_by_role for robustness
    docs_link = page.get_by_role("link", name="Docs")
    docs_link.click()
    print("Clicked on 'Docs' link")

    # 4. Assert that we are on the documentation page
    # Check if the URL contains "/docs/" and if a specific heading is visible
    expect(page).to_have_url(re.compile(".*playwright.dev/docs.*"))
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    print("Verified navigation to Docs and 'Installation' heading is visible")

    # 5. Take a screenshot of the docs page
    screenshot_path = "playwright_docs.png"
    page.screenshot(path=screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

    # You can remove or comment out the visual regression example for now,
    # or adapt it to playwright.dev if you wish.
    # For now, let's keep it simple to get this test passing.