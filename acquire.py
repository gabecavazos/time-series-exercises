import requests
import numpy as np
import pandas as pd



def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return None
    else:
        raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        
        
def get_all_pages(base_url):
    page = 1
    all_data = []
    
    while True:
        url = f"{base_url}?page={page}"
        data = fetch_data(url)
        
        if data is None:
            break
        
        if not data["results"]:
            break

        all_data.extend(data["results"])
        page += 1

    return pd.DataFrame(all_data)