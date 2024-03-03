from bs4 import BeautifulSoup
import requests

from .utils import HEADERS, Job

def scrape_usajobs(job_title: str):
    uri = "https://www.usajobs.gov/search/results/?l=United States&k={}".format(job_title)

    res = requests.get(uri, headers=HEADERS)
    if res.status_code == 403:
        print('USAJOBS: Denied. Counted as a bot')
        return

    # Get the listings
    res_text = BeautifulSoup(res.text, 'html.parser')
    data = res_text.find('div', {'class': 'usajobs-search-results'})
    listings = data.find_all('div', {'class': 'usajobs-search-result--core'})

    job_list = []

    for listing in listings:
        job = Job()
        
        # Company name
        try:
            job.name_of_company = (
                listing
                .find('div', {'class': 'usajobs-search-result--core__body'})
                .find('div', {'class': 'usajobs-search-result--core__summary'})
                .find('h4', {'class': 'usajobs-search-result--core__agency'})
                .text
                .strip()
            )
        except:
            job.name_of_company = None

        # Salary
        try:
            job.salary = (
                listing
                .find('div', {'class': 'usajobs-search-result--core__body'})
                .find('div', {'class': 'usajobs-search-result--core__details'})
                .find('ul', {'class': 'usajobs-search-result--core__details-list'})
                .find('li', {'class': 'usajobs-search-result--core__item'})
                .text
                .strip()
            )
        except:            
            job.salary = None

        # Add job to list
        job_list.append(job)

    print(f'List of jobs and their details for USAJOBS: {job_list}')
