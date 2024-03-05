HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Accept-Language': 'en-US,en;q=0.9,lt;q=0.8,et;q=0.7,de;q=0.6',
}

class Job:
    def __init__(self):
        self.name_of_company: str = None
        self.position: str = None
        self.rating: str = None
        self.salary: str = None
        self.details: str = None

    def print_jobs(job_list):
        for job in job_list:
            print('Company: {}\nPosition: {}\nRating: {}\nSalary: {}\nDetails: {}\n\n'.format(
                job.name_of_company,
                job.position,
                job.rating,
                job.salary,
                job.details
            ))
