from bs4 import BeautifulSoup
import requests

def scrape_monster(job_title):
    uri = "https://monster.com/"
    page = requests.get(uri)
    print(f'monster: {job_title}')
