from bs4 import BeautifulSoup
import requests

from .utils import HEADERS, Job

listing_info = {
    'ul_class': 'JobsList_jobsList__lqjTr',
    'div_class': 'jobCard JobCard_jobCardContent__X81Ew'
}

company_info = {
    'name_class': 'EmployerProfile_employerInfo__d8uSE EmployerProfile_employerWithLogo__E_JPs',
    'name_span': 'EmployerProfile_employerName__qujuA'
}

salary_info = {
    'div_class': 'JobCard_salaryEstimate__arV5J'
}

job_details = {
    'div_class': 'JobCard_jobDescriptionSnippet__yWW8q'
}

def scrape_glassdoor(job_title: str):
    job_title = job_title.replace(' ', '-')

    uri = 'https://www.glassdoor.com/Job/united-states-{}'.format(job_title)

    res = requests.get(uri, headers=HEADERS)
    if res.status_code == 403:
        print('Glassdoor: Denied. Counted as a bot')
        return

    # Get the listings
    res_text = BeautifulSoup(res.text, 'html.parser')
    data = res_text.find('ul', {'class': listing_info['ul_class']})
    listings = data.find_all('div', {'class': listing_info['div_class']})

    job_list = []

    for listing in listings:
        job = Job()

        # Company name
        try:
            job.name_of_company = (
                listing
                .find('div', {'class': company_info['name_class']})
                .find('span', {'class': company_info['name_span']})
                .text
                .strip()
            )
        except:
            job.name_of_company = None

        # Salary
        try:
            job.salary = (
                listing
                .find('div', {'class': salary_info['div_class']})
                .text
                .strip()
            )
        except:            
            job.salary = None

        try:
            job.details = (
                listing
                .find('div', {'class': job_details['div_class']})
                .text
                .strip()
            )
        except:
            job.details = None
        
        # Add job to list
        job_list.append(job)

    print(f'List of jobs and their details for Glassdoor: {job_list}')
