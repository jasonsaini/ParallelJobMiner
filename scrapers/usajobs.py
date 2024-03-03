from bs4 import BeautifulSoup
import requests

def scrape_usajobs(job_title):
    uri = "https://usajobs.gov/"
    # page = requests.get(uri)
    print(f'usa: {job_title}')
