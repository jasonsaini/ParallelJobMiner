from bs4 import BeautifulSoup
import requests

def scrape_indeed(job_title):
    # Change to how Indeed formats urls
    job_title = job_title.replace(' ', '+')
    uri = 'https://www.indeed.com/jobs?q={}&l=United+States'.format(job_title)
    print(uri)
    # page = requests.get(uri)


