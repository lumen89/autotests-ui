from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    password_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input.fill("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    login_button = page.get_by_test_id('registration-page-registration-button')
    login_button.click()

    context.storage_state(path="browser-state.json")



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    expect(page.get_by_test_id('courses-list-toolbar-title-text')).to_have_text("Courses")
    expect(page.get_by_test_id('courses-list-empty-view-title-text')).to_have_text("There is no results")
