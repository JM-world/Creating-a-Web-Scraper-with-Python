from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys      # 한국어 출력 문제로 인한 해결방법
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
import time



options = Options()
options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지 옵션

options.add_argument("--no--sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)

browser.get("https://blog.naver.com/dazerro")

soup = BeautifulSoup(browser.page_source, "html.parser")
time.sleep(3)
job_list = soup.find("tbody", id="postBottomTitleListBody")
time.sleep(3)
print(len(job_list))
# jobs = job_list.find_all("li", recursive=False)  #("li",recursive=False) = 한단계 아래에 있는 li만 찾아 줌.
# # print(len(jobs))

# results = []

# for job in jobs:
#     zone = job.find("div", class_="mosaic")
#     if zone == None:
#         anchor = job.select_one("h2 a")
#         title = anchor["aria-label"]
#         link = anchor["href"]
#         company = job.find("span", class_="companyName")
#         location = job.find("div", class_="companyLocation")
#         job_data = {
#             'company' : company.string,
#             'link' : f"https://www.indeed.com/{link}",
#             'position' : title,
#             'location' : location.string
#         }
#         results.append(job_data)
# for result in results:
#     print(result, "//////\n//////")
        
        
