from http.client import responses

from httpx import Request, RequestNotRead, post, Client


def make_curl_from_request(request: Request) -> str:
    result: list[str] = [f'curl -X {request.method}', f'"{request.url}"']

    for header, value in request.headers.items():
        result.append(f'-H "{header}: {value}"')

    try:
        if body := request.content:
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    return " \\\n".join(result)
    


client = Client()
response = client.get('https://automationexercise.com/api/productsList')

print(make_curl_from_request(response.request))