from ex09_pages import extract_indeed_jobs
from ex06_wwr import extract_wwr_jobs

keyword = input("What do you want to search for?") 

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

for job in jobs:
    print(job)
    print("/////\n/////")