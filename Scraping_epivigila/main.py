import requests
import subprocess


print('Consiguiendo ultima version')

url = "https://raw.githubusercontent.com/superegi/coronavirus_reportePeriodico/main/Scraping_epivigila/scrap_current.py"
resp = requests.get(url)
with open("scrap_current.py", "w") as f:
     f.write(resp.text)

subprocess.call(["python", "scrap_current.py"])
