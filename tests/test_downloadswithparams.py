from playwright.sync_api import Page, Dialog, expect
import pytest

@pytest.mark.parametrize(
    "filename",
    ["some-file.txt", "sample.txt"],
)
def test_download(page: Page, filename: str) -> None:
    page.goto("https://the-internet.herokuapp.com/download", timeout=60000, wait_until="domcontentloaded")
    with page.expect_download() as download_info:
        page.get_by_role("link", name=filename, exact=True).click()
    download = download_info.value
    print(download.suggested_filename)
    assert download.suggested_filename == filename