from bs4 import BeautifulSoup
import requests

def scrape_glassdoor(job_title):
    uri = "https://glassdoor.com/Job/index.htm"
    page = requests.get(uri)
    print(f'glassdoor: {job_title}')
