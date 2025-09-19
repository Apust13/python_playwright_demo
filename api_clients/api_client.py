from typing import Any

import allure
from httpx import Client, URL, QueryParams, Response
from httpx._types import RequestData, RequestFiles, HeaderTypes


class APIClient:
    def __init__(self, client: Client):
        self.client = client


    @allure.step("GET request to {url}")
    def get(
            self,
            url: URL | str,
            params: QueryParams | None = None,
            headers: HeaderTypes | None = None
    ) -> Response:
        return self.client.get(url, params=params, headers=headers)


    @allure.step("POST request to {url}")
    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None,
            headers: HeaderTypes | None = None
    ) -> Response:
        return self.client.post(url, json=json, data=data, files=files, headers=headers)


    @allure.step("PUT request to {url}")
    def put(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        return self.client.put(url, json=json, data=data, files=files)


    @allure.step("DELETE request to {url}")
    def delete(
            self,
            url: URL | str,
            data: RequestData | None = None,
    ) -> Response:
        return self.client.request(method='DELETE', url=url, data=data)