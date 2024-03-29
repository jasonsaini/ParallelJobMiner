import requests

from .utils import Job

def scrape_glassdoor(job_title: str, data_frame):
    url = "https://glassdoor.p.rapidapi.com/jobs/search"

    query_string = {"keyword":job_title, "location_id":"1", "location_type":"N"}

    headers = {
        "X-RapidAPI-Key": "1a706ff713mshe4faa06bd345bdep11a22ejsn6107b481efa1",
        "X-RapidAPI-Host": "glassdoor.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=query_string)

    job_objects = response.json()

    jobs = job_objects.get('hits')

    print(jobs)

    for job_details in jobs:
        job = Job()

        job.title = job_details.get('job_title')

        company_info = job_details.get('company')
        job.company = '' if company_info is None else company_info.get('name')

        job.link = 'glassdoor.com/Job' + job_details.get('link')[4:]

        index = data_frame.get_and_increment_index()
        new_row = ['Glassdoor', job.title, job.company, job.link]
        data_frame.add_new_row(new_row, index)
