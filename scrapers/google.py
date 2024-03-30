from bs4 import BeautifulSoup
import requests

from .utils import HEADERS, Job

listing_info = {
    'ul_class': 'spHGqe',
    'li_class': 'lLd3Je'
}

def scrape_google(job_title, data_frame):
    job_title = job_title.replace(' ', '%20')

    uri = 'https://www.google.com/about/careers/applications/jobs/results/?q="{}"&location=United+States'.format(job_title)

    res = requests.get(uri, headers=HEADERS)
    if res.status_code == 403:
        print('Google: Denied. Counted as a bot')
        return

    # Get the listings
    res_text = BeautifulSoup(res.text, 'html.parser')
    data = res_text.find('ul', {'class': listing_info['ul_class']})
    listings = data.find_all('li', {'class': listing_info['li_class']})

    # For reference later
    # print(listings[0].find('div').find('div', {'class': "Ln1EL"}).find('div', {'class': "VfPpkd-WsjYwc"}).find('div', {'class': "sMn82b"}).find('div', {'class': "ObfsIf-oKdM2c"}).find('div', {'class': "ObfsIf-eEDwDf ObfsIf-eEDwDf-PvhD9-purZT-OiUrBf ObfsIf-eEDwDf-hJDwNd-Clt0zb"}).find('h3', {'class': "QJPWVe"}).text.strip())

    for listing in listings:
        # job = Job()
        # Company name
        try:
            job_title = (
                listing
                .find('div')
                .find('div', {'class': "Ln1EL"})
                .find('div', {'class': "VfPpkd-WsjYwc"})
                .find('div', {'class': "sMn82b"})
                .find('div', {'class': "ObfsIf-oKdM2c"})
                .find('div', {'class': "ObfsIf-eEDwDf ObfsIf-eEDwDf-PvhD9-purZT-OiUrBf ObfsIf-eEDwDf-hJDwNd-Clt0zb"})
                .find('h3', {'class': "QJPWVe"})
                .text
                .strip()
            )
        except:
            job_title = None

        job_link = uri
        company_name = "Google"
        # company_name, job_link
        index = data_frame.get_and_increment_index()
        new_row = ['Google Careers Page', job_title, company_name, job_link]
        data_frame.add_new_row(new_row, index)

