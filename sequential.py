from dotenv import load_dotenv
import os
import threading
import time

# Data frame
from scrapers.utils import ThreadSafeDataframe

# Scrapers
from scrapers import *

# Starts the threads for scraping the sites
def start_scrapers(job_title, data_frame):
    scrapers = {
        scrape_usajobs,
        scrape_indeed,
        scrape_linkedin,
        scrape_glassdoor,
        scrape_github,
        scrape_google,
        scrape_apple,
        scrape_wells_fargo,
    }

    for scraper in scrapers:
        scraper(job_title, data_frame)


if __name__ == "__main__":
    data_frame = ThreadSafeDataframe()

    job_title = os.environ.get('JOB_TITLE')
    start_time = time.time()

    start_scrapers(job_title, data_frame)
    data_frame.convert_df_to_excel('jobs_output_sequential.xlsx')

    elapsed_time = time.time() - start_time
    print(f'Sequential search complete in {elapsed_time:.2f} seconds')
