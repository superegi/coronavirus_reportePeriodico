import requests

url = "path/to/raw/file.csv"
resp = requests.get(url)
with open("scrap01.py", "w") as f:
    f.write(resp.text)
