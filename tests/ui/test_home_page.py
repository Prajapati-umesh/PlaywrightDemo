from pages.base_page import BasePage


def test_navigate_to_homepage(page, config):
    homepage = BasePage(page, config.get_env("base_url"))
    homepage.navigate()
    assert "Example" in page.title()
