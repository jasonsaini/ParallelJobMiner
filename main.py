from bs4 import BeautifulSoup
import multiprocessing as mp, time
import argparse
import requests


def scrape_usajobs(job_title):
    uri = "https://usajobs.gov/"
    page = requests.get(uri)
    print(f'usa: {job_title}')

def scrape_indeed(job_title):
    # Change to how Indeed formats urls
    job_title = job_title.replace(' ', '+')
    uri = "https://indeed.com/"
    page = requests.get(uri)
    print(f'indeed: {job_title}')

def scrape_linkedin(job_title):
    uri = "https://linkedin.com/"
    page = requests.get(uri)
    print(f'linkedin: {job_title}')


def scrape_monster(job_title):
    uri = "https://monster.com/"
    page = requests.get(uri)
    print(f'monster: {job_title}')


def scrape_glassdoor(job_title):
    uri = "https://glassdoor.com/Job/index.htm"
    page = requests.get(uri)
    print(f'glassdoor: {job_title}')


# Starts the threads for scraping the sites
def start_scrapers(job_title):
    scrapers = {
        'usajobs': scrape_usajobs,
        'indeed': scrape_indeed,
        'linkedin': scrape_linkedin,
        'monster': scrape_monster,
        'glassdoor': scrape_glassdoor,
    }

    threads = [
        mp.Process(target=scrapers[site], args=(job_title,))
        for site in scrapers
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


# Gets job title
def get_job():
    parser = argparse.ArgumentParser(description='Job Search CLI')
    parser.add_argument('job_title', type=str, help='Job title to search for')
    args = parser.parse_args()

    return args.job_title


if __name__ == "__main__":
    job_title = get_job()

    print(f'Searching for {job_title} on various job sites...')

    start_time = time.time()

    start_scrapers(job_title)

    elapsed_time = time.time() - start_time
    print(f'Search complete in {elapsed_time:.2f} seconds')
