from playwright.sync_api import Page, Playwright
from .problem_metadata import ProblemMetadata

class Scraper:
    def __init__(self, playwright: Playwright):
        self.__playright__ = playwright

    def __create_page(self) -> Page:
        browser = self.__playright__.chromium.launch(headless=True, channel="chrome", args=["--disable-blink-features=AutomationControlled", "--no-sandbox"])
        ctx = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            locale="en-US",
        )
        page = ctx.new_page()
        return page

    def __open_problem_page(self, page: Page, slug: str) -> None:
        url = f"https://leetcode.com/problems/{slug}/"
        page.goto(url)
        page.wait_for_load_state("networkidle")
    
    def __extract_description(self, page: Page) -> str:
        description_elment = page.locator('div[data-track-load="description_content"]')
        return description_elment.inner_html()
     
    def __extract_difficulty(self, page: Page) -> str:
        difficulty = page.locator('[class*="text-difficulty"]')
        return difficulty.inner_text()
     
    def __close_leet_popup(self, page: Page) -> None:
        popup_close_button = page.locator('button[title="Skip"]')
        if popup_close_button.count() > 0:
            popup_close_button.click()
     
        sidebar_close_button = page.locator('div[title="Close"]')
        if sidebar_close_button.count() > 0:
            sidebar_close_button.click()
     
    def __extract_title(self, page: Page, slug: str) -> str:
        title_selector = f'[href="/problems/{slug}/"]'
        page.wait_for_selector(title_selector)
        return page.inner_text(title_selector)
     
    def __extract_problem_starter(self, page: Page, language: str, snippet_start: str) -> str | None:
        self.__switch_language(page, language)
     
        code_block = page.locator(f'span:has-text("{snippet_start}")')
        code_block.wait_for(state="visible")
     
        code_snippet = ""
        code_lines = page.locator('.view-line')
        for i in range(code_lines.count()):
            line = code_lines.nth(i)
            code_snippet += line.inner_text() + "\n"
        return code_snippet
     
    def __switch_language(self, page: Page, language: str) -> None:
        language_selector = page.locator('button', has_text="C++")
        language_selector.click()
     
        button = page.locator(f'div:text-is("{language}")')
        button.click()

    def extract_metadata(self, slug: str, snippet_start: str = "class Solution:") -> ProblemMetadata:
        page = self.__create_page()
        self.__open_problem_page(page, slug)
        self.__close_leet_popup(page)

        description_html = self.__extract_description(page)
        difficulty = self.__extract_difficulty(page)
        title = self.__extract_title(page, slug)
        problem_starter = self.__extract_problem_starter(page, "Python3", snippet_start)
        if problem_starter is None:
            raise ValueError("Could not extract problem starter code.")

        metadata = ProblemMetadata(
            id=slug,
            title=title,
            difficulty=difficulty,
            content=description_html,
            problem_starter=problem_starter
        )
        return metadata

