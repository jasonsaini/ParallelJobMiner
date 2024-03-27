import requests
import os
from dotenv import load_dotenv
from .utils import Job

load_dotenv('token.env')
api_key = os.getenv('INDEED_KEY')

def scrape_indeed(job_title, data_frame):
    url = "https://indeed11.p.rapidapi.com/"

    payload = {
            "search_terms": job_title,
            "location": "United States",
            "page": "1"
    }
    headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "indeed11.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    job_objects = response.json()
    for job_details in job_objects:
        job = Job()
        job.company = job_details.get('company_name')
        job.title = job_details.get('job_title')
        job.location = job_details.get('location')
        job.link = job_details.get('url')
        index = data_frame.get_and_increment_index()
        new_row = ['Indeed', job.title, job.company, job.link]
        data_frame.add_new_row(new_row, index)

