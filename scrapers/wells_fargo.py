from bs4 import BeautifulSoup
import requests
import math
from .utils import HEADERS, Job

def scrape_wells_fargo(job_title, data_frame):
    og_job_title = job_title.replace(' ', '+')
    uri = 'https://www.wellsfargojobs.com/en/jobs/?page=2&search=Software+Engineer&country=United+States+of+America#results'
    res = requests.get(uri, headers=HEADERS)
    if res.status_code == 403:
        print('Wells Fargo: Denied. Counted as a bot')
        return

    # Get the number of pages
    res_text = BeautifulSoup(res.text, 'html.parser')
    # print(res_text)
    try:
        num_pages_string = res_text\
            .find('p', {'class': 'job-count'})\
            .findAll('strong')[-1]\
            .text\
            .strip()
        num_pages = math.ceil(int(num_pages_string) / 20)
    except:
        num_pages = 0
        print("Wells Fargo Hates Me")

    # For each page, request data from that page and scrape it
    for i in range(0, min(num_pages, 10)):
        uri = 'https://www.wellsfargojobs.com/en/jobs/?page={}&search={}&country=United+States+of+America#results'.format(
            i + 1, og_job_title)
        res = requests.get(uri, headers=HEADERS)
        if res.status_code == 403:
            print('Wells Fargo: Denied. Counted as a bot')
            break

        res_text = BeautifulSoup(res.text, 'html.parser')
        job_table = res_text.find('div', {'class': 'grid job-listing'})
        listings = job_table.find_all('div', {'class': 'card card-job'})

        for listing in listings:
            # job = Job()
            # Company name
            try:
                job_title = (
                    listing
                    .find('a', {'class': 'stretched-link'})
                    .text
                    .strip()
                )
            except:
                job_title = None

            job_link = uri
            company_name = "Wells Fargo"
            index = data_frame.get_and_increment_index()
            new_row = ['Wells Fargo Careers Page', job_title, company_name, job_link]
            data_frame.add_new_row(new_row, index)

