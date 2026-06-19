from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def navigate(self, path: str = "/") -> None:
        self.page.goto(f"{self.base_url.rstrip('/')}/{path.lstrip('/')}")

    def wait_for_element(self, selector: str, timeout: int = 10_000) -> None:
        self.page.wait_for_selector(selector, timeout=timeout)

    def click(self, selector: str) -> None:
        self.wait_for_element(selector)
        self.page.click(selector)

    def enter_text(self, selector: str, text: str) -> None:
        self.wait_for_element(selector)
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        self.wait_for_element(selector)
        return self.page.inner_text(selector)
