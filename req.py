#ПОЗВОЛЯЕТ ПОЛУЧАТЬ ДАННЫЕ С САЙТА

import requests

def get_html(url): 
    try:
        result=requests.get(url)
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestException as e: # если сеть выключилась
            print(e)
            return False
