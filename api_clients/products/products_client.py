from httpx import Response

from api_clients.api_client import APIClient
from api_clients.authentication.authentication_schema import AuthenticationUserSchema
from api_clients.private_http_builder import get_private_http_client
from api_clients.public_http_builder import get_public_http_client
from utils.api_routes import ApiRoute


class ProductsClient(APIClient):
    def get_all_products_list_api(self) -> Response:
        return self.get(ApiRoute.PRODUCTS_LIST)

    def search_product_api(self, product: str) -> Response:
        payload = {"search_product":product}
        return self.post(ApiRoute.SEARCH_PRODUCT, data=payload)

    def search_product(self, product: str):
        response = self.search_product_api(product)
        return response.json()

    def get_all_products(self):
        response = self.get_all_products_list_api()
        return response.json()


def get_product_client() -> ProductsClient:
    return ProductsClient(client=get_public_http_client())

def get_private_products_client(user: AuthenticationUserSchema) -> ProductsClient:
    return ProductsClient(client=get_private_http_client(user))