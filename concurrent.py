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
        'github': scrape_github,
        'usajobs': scrape_usajobs,
        'indeed': scrape_indeed,
        'linkedin': scrape_linkedin,
        'glassdoor': scrape_glassdoor,
        'google': scrape_google,
        'apple': scrape_apple,
    }
    threads = [
        threading.Thread(target=scrapers[site], args=(job_title, data_frame))
        for site in scrapers
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    data_frame = ThreadSafeDataframe()

    job_title = os.environ.get('JOB_TITLE')
    start_time = time.time()

    start_scrapers(job_title, data_frame)
    data_frame.convert_df_to_excel('jobs_output.xlsx')

    elapsed_time = time.time() - start_time
    print(f'Concurrent Search complete in {elapsed_time:.2f} seconds')
