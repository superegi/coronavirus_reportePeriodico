# -*- coding: latin-1 -*-
import requests
import subprocess


print('Consiguiendo ultima version')

url = "http://raw.githubusercontent.com/superegi/coronavirus_reportePeriodico/main/Scraping_epivigila/MAIN.py"
resp = requests.get(url)
with open("MAIN.py", "w" ,encoding="utf-8") as f:
     f.write(resp.text)

subprocess.call(["python", "MAIN.py"])
print('listo')