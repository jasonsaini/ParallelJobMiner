import requests
import os
from dotenv import load_dotenv

from .utils import Job

load_dotenv('token.env')
api_key = os.getenv('LINKEDIN_KEY')

def scrape_linkedin(job_title: str):
    url = 'https://linkedin-jobs-search.p.rapidapi.com/'

    payload = {
        'search_terms': job_title,
        'location': 'United States',
        'page': '1'
    }

    headers = {
        'content-type': 'application/json',
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'linkedin-jobs-search.p.rapidapi.com'
    }

    response = requests.post(url, json=payload, headers=headers)

    job_objects = response.json()
    job_list = []

    for job_details in job_objects:
        job = Job()
        job.company = job_details.get('normalized_company_name')
        job.title = job_details.get('job_title')
        job.location = job_details.get('job_location')
        job.link = job_details.get('linkedin_job_url_cleaned')

        job_list.append(job)

    Job.print_jobs(job_list)
