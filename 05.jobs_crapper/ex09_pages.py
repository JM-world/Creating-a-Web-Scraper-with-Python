from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys      # 한국어 출력 문제로 인한 해결방법
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

options = Options()
options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지 옵션

options.add_argument("--no--sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)


def get_page_count(keyword):
    browser.get(f"https://www.indeed.com/jobs?q={keyword}&limit=5")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("ul", class_="pagination-list")
    if pagination == None:
        return 1
    pages = pagination.find_all("li", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count


def extract_indeed_job(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        browser.get(f"https://www.indeed.com/jobs?q={keyword}&start={page*10}")

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="css-zu9cdh")
        #print(len(job_list))
        jobs = job_list.find_all("li", recursive=False)  #("li",recursive=False) = 한단계 아래에 있는 li만 찾아 줌.
        # print(len(jobs))

        

        for job in jobs:
            zone = job.find("div", class_="mosaic")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor["aria-label"]
                link = anchor["href"]
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link' : f"https://www.indeed.com/{link}",
                    'company' : company.string.replace(",", " "),  #엑셀 행이 초과할때 replace로 고쳐주기
                    'location' : location.string.replace(",", " "),
                    'position' : title.replace(",", " ")
                }
                results.append(job_data)
    return results
            