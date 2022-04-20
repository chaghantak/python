import requests
from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs/companies?q=python"


def get_last_page():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page= pages[-2].get_text(strip=True)
    return last_page

def extract_jobs(last_page):
    jobs=[]

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
