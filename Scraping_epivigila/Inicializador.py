# -*- coding: latin-1 -*-
import requests
import subprocess


print('Consiguiendo ultima version')

url = "https://raw.githubusercontent.com/superegi/coronavirus_reportePeriodico/main/Scraping_epivigila/MAIN.py"
resp = requests.get(url)
with open("MAIN.py", "wb") as f:
     f.write(resp.text)

subprocess.call(["python", "MAIN.py"])
