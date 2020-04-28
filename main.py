from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import sqlite3

conn = sqlite3.connect("corona.db")
c =conn.cursor()

try:
    c.execute("""CREATE TABLE corona(country text , t_cases text , n_cases text , t_deaths text , n_deaths text , t_recovered text , active_cases text , serious text , t_tests text , continent)""")
    print("Created Table")
except:
    print("Table already created")
    print("Deleting table")
    c.execute("""DROP TABLE corona""")
    print("Creating table")
    c.execute("""CREATE TABLE corona(country text , t_cases text , n_cases text , t_deaths text , n_deaths text , t_recovered text , active_cases text , serious text , t_tests text , continent)""")
    print("Created Table")


url = "https://www.worldometers.info/coronavirus/#countries"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}


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
        print("INSERT INTO corona values("+country+","+t_cases+")")
        c.execute("INSERT INTO corona values('"+country+"','"+ t_cases+"','"+ n_cases+"','"+ t_deaths+"','"+ n_deaths+"','"+ t_recovered+"','"+ active_cases+"','"+ serious+"','"+ t_tests+"','"+continent+"')")
    
    def all(country_name):
        c.execute("select * from corona where country='"+country_name+"'")
        return c.fetchall()


req = Request(url=url, headers=headers)
html = urlopen(req).read()

souped = soup(html, "html.parser")


table = souped.find("table", {"id":"main_table_countries_today"})

world_report = table.tbody.find_all("tr")
arr1 = []
for i in range(7, len(world_report)):
    for b in world_report[i].find_all("td"):
        print(b.text)
        arr1.append(b.text)
    a = corona_stats(arr1[0], arr1[1], arr1[2], arr1[3], arr1[4], arr1[5], arr1[6], arr1[7], arr1[8], arr1[9], arr1[10], arr1[11],arr1[12] )
    del arr1[:]




 
 

c.execute("select * from corona where country='Germany'")
c.fetchall()
conn.commit()
