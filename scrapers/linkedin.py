from bs4 import BeautifulSoup
import requests

def scrape_linkedin(job_title):
    uri = "https://linkedin.com/"
    page = requests.get(uri)
    print(f'linkedin: {job_title}')
