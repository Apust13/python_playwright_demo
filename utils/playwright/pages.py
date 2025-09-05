from datetime import datetime, timezone

import allure
from playwright.sync_api import Playwright, Page
from config import settings, Browser
from utils.playwright.mocks import mock_static_resources


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,
        storage_state: str | None = None
)-> Page:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    mock_static_resources(page)

    yield page

    timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    filename = f'{test_name}-{timestamp}.zip'

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{filename}'))

    browser.close()

    allure.attach.file(settings.tracing_dir.joinpath(f'{filename}'), name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)