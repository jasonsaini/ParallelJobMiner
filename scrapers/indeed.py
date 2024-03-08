from bs4 import BeautifulSoup
import requests

from .utils import HEADERS, Job

def scrape_indeed(job_title: str):
    job_list = []

    # Change to how Indeed formats job titles for uri
    job_title = job_title.replace(' ', '+')

    uri = 'https://www.indeed.com/jobs?q={}&l=United+States'.format(job_title)

    res = requests.get(uri, headers=HEADERS)
    if res.status_code == 403:
        print('Indeed: Denied. Counted as a bot')
        return

    # Get the listings
    res_text = BeautifulSoup(res.text, 'html.parser')
    data = res_text.find('ul', {'class': 'css-zu9cdh'})
    listings = data.find_all('div', {'class': 'cardOutline'})

    for listing in listings:
        job = Job()

        # Company name
        try:
            job.name_of_company = (
                listing
                .find('div', {'class': 'companyInfo'})
                .find('span', {'class':'companyName'})
                .text
                .strip()
            )
        except:
            job.name_of_company = None

        # Rating
        try:
            job.rating = (
                listing
                .find('div', {'class': 'companyInfo'})
                .find('span', {'class': 'ratingsDisplay'})
                .text
                .strip()
            )
        except:
            job.rating = None

        # Salary
        try:
            job.salary = (
                listing
                .find('div', {'class': 'salary-snippet-container'})
                .text
                .strip()
            )
        except:
            job.salary = None

        # Job details
        try:
            job.job_details = (
                listing
                .find('div', {'class': 'metadata taxoAttributes-container'})
                .find('ul')
                .text
                .strip()
            )
        except:
            job.job_details = None
        
        # Add job to list
        job_list.append(job)

    print(f'List of jobs and their details for Indeed: {job_list}')
