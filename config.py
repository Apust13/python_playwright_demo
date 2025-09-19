import sys
from enum import Enum
from typing import Self

from pydantic import BaseModel, EmailStr, HttpUrl
from pydantic.types import FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = 'webkit'
    FIREFOX = 'firefox'
    CHROMIUM = 'chromium'

class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str

class TestData(BaseModel):
    image_png_file: FilePath

class HTTPClientConfig(BaseModel):
    api_base_url: HttpUrl
    timeout: float
    proxy_url: HttpUrl

    @property
    def client_url(self):
        return str(self.api_base_url)

    @property
    def proxy(self):
        return str(self.proxy_url)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='./.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    http_client: HTTPClientConfig
    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_user2: TestUser
    test_user3: TestUser
    test_data: TestData
    allure_results_dir: DirectoryPath
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath

    def get_base_url(self) -> str:
        return f'{self.app_url}/'


    @classmethod
    def initialize(cls) -> Self:
        if "--headed" in sys.argv:
            headless_override = False
        elif "--headless" in sys.argv:
            headless_override = True
        else:
            headless_override = None

        videos_dir = DirectoryPath('./video')
        tracing_dir = DirectoryPath('./tracing')
        browser_state_file = FilePath('./browser-state.json')
        allure_results_dir = DirectoryPath('./allure-results')

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)

        base_settings = cls(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file
        )

        if headless_override is not None:
            base_settings.headless = headless_override

        return base_settings

settings = Settings.initialize()
