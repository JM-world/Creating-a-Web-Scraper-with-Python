from ex09_pages import extract_indeed_jobs
from ex06_wwr import extract_wwr_jobs

keyword = input("What do you want to search for?") 

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

for job in jobs:
    print(job)
    print("//////\n//////")

file = open(f"{keyword}.scv", "w")   #UnicodeEncodeError 'cp949' codec can't encode character 오류 날 시, file = open(f"{keyword}.csv", "w", encoding="utf-8")로 수정하기.
                                     # 이후 엑셀에서도 깨질 떈, file = open(f"{keyword}.csv", "w", encoding="utf-8-sig")로 변경.
file.write("Position,Company,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()
            