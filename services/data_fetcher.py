import requests

def get_market_data(sector):
    url = f"https://api.duckduckgo.com/?q={sector}+India+market+news&format=json"
    response = requests.get(url)
    return response.json()