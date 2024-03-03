from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
#from .utils import HEADERS, Job

load_dotenv('token.env')
api_key = os.getenv('USAJOBS_KEY')

# Manually read and print the contents of token.env
with open('token.env') as file:
    for line in file:
        print(line.strip())


def scrape_usajobs(job_title, api_key):
    base_url = "https://data.usajobs.gov/api/search"
    headers = {
        "User-Agent": "your_email@example.com",  # Replace with your email
        "Authorization-Key": api_key
    }
    params = {
        "Keyword": job_title
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

        print(f"Job Title: {job_title}\nCompany: {company_name}\nLink: {job_link}\n")
 # Replace with your actual API key
scrape_usajobs("Software Engineer", api_key)


# def scrape_usajobs(job_title: str):
#     uri = "https://www.usajobs.gov/search/results/?l=United States&k={}".format(job_title)

#     res = requests.get(uri, headers=HEADERS)
#     if res.status_code == 403:
#         print('USAJOBS: Denied. Counted as a bot')
#         return

#     # Get the listings
#     res_text = BeautifulSoup(res.text, 'html.parser')
#     data = res_text.find('div', {'class': 'usajobs-search-results'})
#     listings = data.find_all('div', {'class': 'usajobs-search-result--core'})

#     job_list = []

#     for listing in listings:
#         job = Job()
        
#         # Company name
#         try:
#             job.name_of_company = (
#                 listing
#                 .find('div', {'class': 'usajobs-search-result--core__body'})
#                 .find('div', {'class': 'usajobs-search-result--core__summary'})
#                 .find('h4', {'class': 'usajobs-search-result--core__agency'})
#                 .text
#                 .strip()
#             )
#         except:
#             job.name_of_company = None

#         # Salary
#         try:
#             job.salary = (
#                 listing
#                 .find('div', {'class': 'usajobs-search-result--core__body'})
#                 .find('div', {'class': 'usajobs-search-result--core__details'})
#                 .find('ul', {'class': 'usajobs-search-result--core__details-list'})
#                 .find('li', {'class': 'usajobs-search-result--core__item'})
#                 .text
#                 .strip()
#             )
#         except:            
#             job.salary = None

#         # Add job to list
#         job_list.append(job)

#     print(f'List of jobs and their details for USAJOBS: {job_list}')

