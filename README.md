# Parallel Job Miner 🔍💼
### By: Joshua Byrd, Jason Saini, Brendan Smith, Parker Waller,  David Santamaria

---

## 📝 Description
A web scraper that searches for your dream job position across major platforms:
-  Apple
-  Github/Simplify 
-  Glassdoor
-  Google
-  Indeed
-  LinkedIn
-  USAJOBS
-  Wells Fargo
It fetches info on available listings and the number of positions listed, making your job hunt efficient and streamlined!

---

## 🛠 Installation

Ensure you have python3.

Clone and set up with ease:
```
git clone https://github.com/jasonsaini/ParallelJobMiner.git **or** 
git clone git@github.com:jasonsaini/ParallelJobMiner.git

cd ParallelJobMiner
pip install -r requirements.txt
python3 main.py "Job Title"   (ex: python3 main.py "software engineer")
```

---

## 🚀 Highlights from our Paper

- 📈 **Technique**: Leveraging BeautifulSoup, RapidAPI, and Python's multiprocessing library, we crafted a multi-threaded web scraper that's both powerful and efficient.

- 🤔 **Challenges**: Navigating anti-scraping measures, managing API token limits, and improving user experience were our major hurdles.

- 💡 **Solution**: We used official APIs for reliable data scraping and created a thread-safe extended class for our pandas dataframe.

- 📊 **Efficiency**: Our concurrent algorithm significantly reduces runtime compared to sequential methods, leading to quicker job application compilation.

- 🔍 **Next Steps**: Enhancing the UX/UI, filtering duplicates, and extending the scraper's capabilities are our focus areas.

- 🌟 **Conclusion**: Aiming to ease the job search process for computer science students and professionals, we're dedicated to continuous improvement and user empowerment.

---

## ✅ TODO

- [X] Finish scraping/querying remaining sites (Monster, Glassdoor, Indeed).
- [X] Investigate multi-threaded ways to append Excel data for potential performance improvements.
- [ ] Implement a method to filter out duplicate positions from multiple sites.
- [X] Navigate and resolve API token limits (e.g., LinkedIn's 25 queries/month limit).
- [ ] Add a legend to the spreadsheet to enable color-coded status tracking for job applications.
- [ ] Introduce more parameters to customize the job search further.
- [ ] Stretch Goal: Implement better UI/UX improvements.

---

## 🤝 Contribute
Join our mission in making job hunting a breeze. Your ideas and contributions are welcome!
