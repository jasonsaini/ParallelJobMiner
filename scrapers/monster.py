from bs4 import BeautifulSoup
import requests

from .utils import HEADERS, Job

listing_info = {
    'ul_class': 'sc-harTkY jEHPnr',
    'div_class': 'job-search-resultsstyle__JobCardWrap-sc-1wpt60k-4 gFeVEp'
}

company_info = {
    'outer_div_class': 'sc-gwZKzw evWkPy',
    'inner_div_class': 'sc-bSiGmx LCGfq',
    'heading_class': 'sc-eTqNBC kPYuOz',
}

salary_info = {
    'div_class': 'JobCard_salaryEstimate__arV5J'
}

job_details = {
    'div_class': 'JobCard_jobDescriptionSnippet__yWW8q'
}

def scrape_monster(job_title):
    job_title = job_title.replace(' ', '+')

    uri = 'https://www.monster.com/jobs/search?q={}&where=United+States&page=1'.format(job_title)

    res = requests.get(uri, headers=HEADERS)
    if res.status_code == 403:
        print('Monster: Denied. Counted as a bot')
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
                .find('div', {'class': company_info['outer_div_class']})
                .find('div', {'class': company_info['inner_div_class']})
                .find('h3', {'class': company_info['heading_class']})
                .text
                .strip()
            )
        except:
            job.name_of_company = None
        
        # Add job to list
        job_list.append(job)

    print(f'List of jobs and their details: {job_list}')
