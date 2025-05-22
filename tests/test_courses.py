import pytest
from playwright.sync_api import expect, Page

@pytest.mark.courses
def test_empty_courses_list_with_fixt(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    expect(chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')).to_have_text("Courses")
    expect(chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')).to_have_text("There is no results")
