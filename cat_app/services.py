import requests


def cat():
    url = 'https://api.thecatapi.com/v1/images/search'
    params = {'x-api-key':'0f5e1a22-d089-47be-94e3-a0a2d4df6b62'}
    response = requests.get(url, params = params)
    r = response.json()
    return r[0]['url']
