import multiprocessing as mp, time
import argparse

from scrapers import scrape_glassdoor
from scrapers import scrape_indeed
from scrapers import scrape_linkedin
from scrapers import scrape_monster
from scrapers import scrape_usajobs

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
