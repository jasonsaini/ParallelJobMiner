import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the GitHub page to be scraped
url = 'https://github.com/SimplifyJobs/Summer2024-Internships'

# Perform an HTTP request to get the HTML content of the page
response = requests.get(url)
html_content = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the README section
readme_section = soup.find('article', class_='markdown-body entry-content container-lg')

# Initialize lists to store the scraped data
job_titles = []
companies = []
locations = []
links = []
apply_dates = []

# Check if the README section is found
if readme_section:
    # Find the first table within the README section
    table = readme_section.find('table')
    
    if table:
        # Iterate through each row of the table, except for the header
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) >= 5:  # Ensure that there are enough columns
                # Check if the link column has an 'a' tag
                link_tag = columns[3].find('a', href=True)
                if link_tag:
                    # Get company name, job title, location, apply link, and apply date
                    company = columns[0].text.strip()
                    job_title = columns[1].text.strip()
                    location = columns[2].text.strip()
                    link = link_tag['href']
                    apply_date = columns[4].text.strip()

                    # Append data to the lists
                    companies.append(company)
                    job_titles.append(job_title)
                    locations.append(location)
                    links.append(link)
                    apply_dates.append(apply_date)
    else:
        print("Table not found in the README section")
else:
    print("README section not found")

# Create a DataFrame from the scraped data
df = pd.DataFrame({
    'Company': companies,
    'Job Title': job_titles,
    'Location': locations,
    'Link': links,
    'Apply Date': apply_dates
})

print(df)
