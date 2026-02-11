import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://api.nasa.gov/"
page = requests.get(url)

print(page.status_code)
print(page.content)
#print(page.json())
key = "3Sf1TZ4c3ra9bTAh7gCiFaUnNML5BC1k0t5WypQB"
params = {
    "api_key" : key
}
ph=requests.get("https://api.nasa.gov/planetary/apod", params=params)
print(ph.status_code)
print(ph.content)
print(ph.json())
print ("_________________________________________________________________")
soop=BeautifulSoup(ph.content,"html.parser")
print(soop.prettify())
print("____________________________________________________________________")
par = {
    "api_key": key,
    "start_date": "2024-01-01",
    "end_date": "2024-01-02"
}
new = requests.get("https://api.nasa.gov/neo/rest/v1/feed", params=par)
print(new.json().keys)
print(new.status_code)
#print(new.content)
#print(new.json().keys())
donner=[]
if new.status_code == 200:
    data = new.json()
    for d in data["near_earth_objects"]:
        for ast in data["near_earth_objects"][d]:
            id=ast["id"]
            name=ast["name"]
            diameter=float(ast["estimated_diameter"]["kilometers"]["estimated_diameter_min"])
            Magnitude =ast['absolute_magnitude_h']
            v_relative=float(ast["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"])
            donner.append({"id":id,"name":name,"diametre":diameter,"magnitude":Magnitude,"relative_velocity":v_relative})

data_set=pd.DataFrame(donner)
data_set.to_csv("scraping_test.scv", index=False)
print(data_set.head())