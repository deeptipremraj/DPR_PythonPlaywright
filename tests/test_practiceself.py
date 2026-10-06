import re
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.external
def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_role("textbox", name="First Name").fill("John")
    page.get_by_role("textbox", name="Last Name").fill("Doe")
    page.get_by_role("textbox", name="name@example.com").fill("john.doe@example.com")
    page.get_by_role("radio", name="Male", exact=True).check()
    page.get_by_role("textbox", name="Mobile Number").fill("1234567878")
    page.locator("#subjectsContainer div").nth(3).click()
    page.locator("div").filter(has_text=re.compile(r"^Sports$")).click()
    page.locator("#uploadPicture").set_input_files("test-data/BhumikaPremSchedule.PNG")
    page.get_by_role("textbox", name="Current Address").fill("123 Main St, Anytown, USA")
    page.locator("#state > .css-13cymwt-control > .css-hlgwow > .css-19bb58m").click()
    page.locator("div").filter(has_text=re.compile(r"^Select City$")).first.click()
    page.get_by_role("button", name="Submit").click()
    assert page.get_by_text("Thanks for submitting the form").is_visible()
    page.get_by_role("button", name="Close").click()
