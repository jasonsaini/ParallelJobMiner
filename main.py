import multiprocessing
import multiprocessing as mp, time
import argparse
import threading
import pandas as pd
import os
from scrapers import scrape_usajobs
import requests
from dotenv import load_dotenv
from scrapers import scrape_glassdoor
from scrapers import scrape_indeed
from scrapers import scrape_linkedin
from scrapers import scrape_monster


# Starts the threads for scraping the sites
def start_scrapers(job_title, data_frame):
    scrapers = {
        'usajobs': scrape_usajobs
        # 'indeed': scrape_indeed,
        # 'linkedin': scrape_linkedin,
        # 'monster': scrape_monster,
        # 'glassdoor': scrape_glassdoor,
    }

    threads = [
        threading.Thread(target=scrapers[site], args=(job_title, data_frame))
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


class ThreadSafeDataframe:
    excel_header = ["Site", "Job Title", "Company", "Link"]

    def __init__(self):
        self.lock = threading.Lock()
        self.index = 0
        self.df = pd.DataFrame(columns=self.excel_header)

    def print_df(self):
        print(self.df)

    def get_and_increment_index(self):
        with self.lock:
            self.index += 1
            return self.index

    def convert_df_to_excel(self):
        exists = os.path.isfile('./jobs_output.xlsx')
        if exists:
            writer = pd.ExcelWriter('jobs_output.xlsx', mode='a', if_sheet_exists='replace')
        else:
            writer = pd.ExcelWriter('jobs_output.xlsx')
        self.df.to_excel(writer, sheet_name='jobs_list')
        writer.close()

    def add_new_row(self, new_row, index):
        print(f'{index}: {new_row}')
        self.df.loc[index] = new_row


if __name__ == "__main__":
    job_title = get_job()

    print(f'Searching for {job_title} on various job sites...')
    data_frame = ThreadSafeDataframe()

    start_time = time.time()

    start_scrapers(job_title, data_frame)
    data_frame.convert_df_to_excel()

    elapsed_time = time.time() - start_time
    print(f'Search complete in {elapsed_time:.2f} seconds')
