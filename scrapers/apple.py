from bs4 import BeautifulSoup
import requests
import math
from .utils import HEADERS, Job

def scrape_apple(job_title, data_frame):
    og_job_title = job_title.replace(' ', '%20')
    uri = 'https://jobs.apple.com/en-us/search?search=Software%20Engineer&sort=relevance&location=united-states-USA'
    res = requests.get(uri, headers=HEADERS)
    if res.status_code == 403:
        print('Apple: Denied. Counted as a bot')
        return

    # Get the number of pages
    res_text = BeautifulSoup(res.text, 'html.parser')
    print(uri)

    try:
        num_pages_string = res_text.find('h2', {'id': 'resultCount'})\
            .find('span')\
            .text\
            .strip()
        print(num_pages_string)

        found_num_pages = False
        string_index = 1
        # Num pages is found in text that looks like this: 600+ Result(s), so find where it stops being a number,
        # convert to an int, and divide by number of entries per page to get total number of pages to search
        for idx, c in enumerate(num_pages_string):
            if not c.isnumeric():
                string_index = idx
                found_num_pages = True
                break
        if found_num_pages:
            num_pages = math.floor(int(num_pages_string[:int(string_index)]) / 20)
        else:
            num_pages = 1
        print(num_pages)
    except:
        num_pages = 1
        print("Apple Hates Me")

    # For each page, request data from that page and scrape it

    for i in range(0, min(10, num_pages)):
        uri = 'https://jobs.apple.com/en-us/search?location=united-states-USA&search={}&sort=relevance&page={}'.format(
            og_job_title, i + 1)
        res = requests.get(uri, headers=HEADERS)
        if res.status_code == 403:
            print('Apple: Denied. Counted as a bot')
            break

        res_text = BeautifulSoup(res.text, 'html.parser')
        job_table = res_text.find('table', {'id': 'tblResultSet'})
        listings = job_table.find_all('tbody')

        # For reference later
        # print(listings[0].find('div').find('div', {'class': "Ln1EL"}).find('div', {'class': "VfPpkd-WsjYwc"}).find('div', {'class': "sMn82b"}).find('div', {'class': "ObfsIf-oKdM2c"}).find('div', {'class': "ObfsIf-eEDwDf ObfsIf-eEDwDf-PvhD9-purZT-OiUrBf ObfsIf-eEDwDf-hJDwNd-Clt0zb"}).find('h3', {'class': "QJPWVe"}).text.strip())

        for listing in listings:
            # job = Job()
            # Company name
            try:
                job_title = (
                    listing
                    .find('td', {'class': 'table-col-1'})
                    .find('a', {'class': 'table--advanced-search__title'})
                    .text
                    .strip()
                )
            except:
                job_title = None

            try:
                job_link_end = (
                    listing
                    .find('td', {'class': 'table-col-1'})
                    .find('a', {'class': 'table--advanced-search__title'})
                    .get('href')
                )
                job_link = 'https://jobs.apple.com' + job_link_end
            except:
                job_link = uri

            company_name = "Apple"
            index = data_frame.get_and_increment_index()
            new_row = ['Apple Careers Page', job_title, company_name, job_link]
            data_frame.add_new_row(new_row, index)

