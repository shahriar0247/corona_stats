from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.worldometers.info/coronavirus/#countries"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}


req = Request(url=url, headers=headers)
html = urlopen(req).read()

souped = soup(html, "html.parser")

countries = souped.findAll("a", {"class":"mt_a"})
total_deaths = souped.find("table", {"class":"main_table_countries"})
table = souped.find("table", {"id":"main_table_countries_today"})

world_report = table.tbody.find_all("tr")[8]



class corona_stats:
    def __init__(self, country, t_cases, n_cases, t_deaths, n_deaths, t_recovered, active_cases, serious, lol, lol2, t_tests, lol3, continent):
        self.country = country
        self.t_cases = t_cases
        self.n_cases = n_cases
        self.t_deaths = t_deaths
        self.n_deaths = n_deaths
        self.t_recovered = t_recovered
        self.active_cases = active_cases
        self.serious = serious
        self.t_tests = t_tests
        self.continent = continent
    
    def country(self):
        return self.country
    def t_cases(self):
        return self.t_cases
    def n_cases(self):
        return self.n_cases
    def t_deaths(self):
        return self.t_deaths
    def n_deaths(self):
        return self.n_deaths
    def t_recovered(self):
        return self.t_recovered
    def active_cases(self):
        return self.active_cases
    def serious(self):
        return self.serious
    def t_tests(self):
        return self.t_tests
    def continent(self):
        return self.continent
 

b = corona_stats(world_report[0],world_report[1],world_report[2]... upto world_report[9])


