#test case 1 - click action

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.external
def test_add_remove_elements(page: Page) -> None:
    delete_button = page.get_by_role("button", name="Delete") 
    add_element_button = page.get_by_role("button", name="Add Element")
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/",timeout=60000, wait_until="domcontentloaded")   
    add_element_button.click()
    #add_element_button.click()
    delete_button.first.click()
    assert delete_button.is_visible
    #assert delete_button.count() == 1
    
@pytest.mark.external
def test_fill_and_press_enter(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/login", timeout=60000, wait_until="domcontentloaded")
    username_field = page.get_by_role("textbox", name="Username")
    password_field = page.get_by_role("textbox", name="Password")
    login_button = page.get_by_role("button", name="Login")
    username_field.fill("tomsmith")
    username_field.press("Tab")
    password_field.fill("SuperSecretPassword!")
    password_field.press("Tab")
    password_field.press("Enter")
    #login_button.click()
    actual_text = page.get_by_role("heading", name="Welcome to the Secure Area.").text_content()
    expected_text = "Welcome to the Secure Area. When you are done click logout below"
    assert expected_text in actual_text

def test_checkboxes(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/checkboxes", timeout=60000, wait_until="domcontentloaded")
    boxes = page.get_by_role("checkbox")
    boxes.first.check()
    boxes.last.uncheck()
    assert boxes.first.is_checked()
    assert not boxes.last.is_checked()

def test_dropdown(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dropdown", timeout=60000, wait_until="domcontentloaded")
    dropdown = page.locator("#dropdown")
    dropdown.select_option(label="Option 1")
    dropdown.select_option("Option 2")

def test_hover(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/hovers", timeout=60000, wait_until="domcontentloaded")
    # images = page.get_by_role("img")
    # images.first.hover()
    # images.last.hover()
    image = page.locator(".figure").first
    image.hover() 

def test_upload(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/upload", timeout=60000, wait_until="domcontentloaded")
    page.locator("#file-upload").set_input_files("test-data/test.txt")
    page.locator("#file-submit").click()

def test_drag_and_drop(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/drag_and_drop", timeout=60000, wait_until="domcontentloaded")
    source = page.locator("#column-a")
    target = page.locator("#column-b")
    source.drag_to(target)
    target.drag_to(source)
    

def test_context_menu_2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/context_menu", timeout=60000, wait_until="domcontentloaded")
    page.locator("#hot-spot").click()
    #page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator("#hot-spot").click(button="right")
    assert page.get_by_text("Context menu items are custom").is_visible()

@pytest.mark.external
def test_download(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/download", timeout=60000, wait_until="domcontentloaded")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="some-file.txt", exact=True).click()
    download = download_info.value
    print(download.suggested_filename)
    assert download.suggested_filename == "some-file.txt"

@pytest.mark.external
def test_entry_ad(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/entry_ad", timeout=60000, wait_until="domcontentloaded")
    modal = page.locator("#modal")
    modal.wait_for(state="visible")
    assert modal.is_visible()
    modal.wait_for(timeout=10000)
    page.get_by_text("Close", exact=True).click()
    modal.wait_for(state="hidden")
    assert not modal.is_visible()

    