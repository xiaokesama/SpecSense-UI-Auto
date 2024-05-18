import requests


def send_http_request(url,method,**kwargs) -> requests.Response:
    method = method.lower()
    return getattr(requests,method)(url,**kwargs)


if __name__ == '__main__':
    response = send_http_request('http://127.0.0.1:8000','get')
    print(response.status_code)