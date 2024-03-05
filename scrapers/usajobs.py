from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
#from .utils import HEADERS, Job

load_dotenv('token.env')
api_key = os.getenv('USAJOBS_KEY')


def scrape_usajobs(job_title, data_frame):
    base_url = "https://data.usajobs.gov/api/search"
    headers = {
        "User-Agent": "your_email@example.com",  # Replace with your email
        "Authorization-Key": api_key
    }
    params = {
        "Keyword": job_title,
        "Series": "1550,2210"
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        print("Failed to retrieve data from USAJobs")
        return

    data = response.json()
    job_listings = data.get('SearchResult', {}).get('SearchResultItems', [])
    print("USAJOBS Listings:")
    for job in job_listings:
        job_title = job['MatchedObjectDescriptor']['PositionTitle']
        company_name = job['MatchedObjectDescriptor']['OrganizationName']
        job_link = job['MatchedObjectDescriptor']['PositionURI']
        index = data_frame.get_and_increment_index()
        new_row = ['USAJobs', job_title, company_name, job_link]
        data_frame.add_new_row(new_row, index)
