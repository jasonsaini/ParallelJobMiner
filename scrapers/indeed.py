from bs4 import BeautifulSoup
import requests

job_list = {}
job = {}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Accept-Language': 'en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6',
}

def scrape_indeed(job_title: str):
    # Change to how Indeed formats job titles for uri
    job_title = job_title.replace(' ', '+')

    uri = 'https://www.indeed.com/jobs?q={}&l=United+States'.format(job_title)

    res = requests.get(uri, headers=HEADERS)
    if res.status_code == 403:
        print('Indeed: Denied. Counted as a bot')
        return

    # Get the listings
    res_text = BeautifulSoup(res.text, 'html.parser')
    data = res_text.find('ul', {'class': 'css-zu9cdh'})
    listings = data.find_all('div', {'class': 'cardOutline'})

    for i in range(0, len(listings)):
        # Company name
        try:
            job["name-of-the-company"] = listings[i].find("div",{"class":"companyInfo"}).find("span",{"class":"companyName"}).text
        except:
            job["name-of-the-company"] = None

        # Rating
        try:
            job["rating"] = listings[i].find("div",{"class":"companyInfo"}).find("span",{"class":"ratingsDisplay"}).text
        except:
            job["rating"] = None

        # Salary
        try:
             job["salary"] = listings[i].find("div",{"class":"salary-snippet-container"}).text
        except:            
             job["salary"] = None

        try:
            job["job-details"] = listings[i].find("div",{"class":"metadata taxoAttributes-container"}).find("ul").text
        except:
            job["job-details"] = None
        
        # Add job to list
        job_list.append(job)

    print(f'List of jobs and their details: {job_list}')
