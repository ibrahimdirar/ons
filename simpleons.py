import requests
import os

r_rpi = requests.get(
    "https://api.ons.gov.uk/dataset/mm23/timeseries/CHAW/data")
r_cpi = requests.get(
    "https://api.ons.gov.uk/dataset/mm23/timeseries/D7BT/data")
r_rpix = requests.get(
    "https://api.ons.gov.uk/dataset/mm23/timeseries/CHMK/data")

print("Next release: " + r_rpi.json()['description']['nextRelease'])

print(r_rpi.json()['description']['date'] +
      " - " + r_rpi.json()['description']['title'])
print(r_rpi.json()['description']['number'])

print(r_cpi.json()['description']['date'] +
      " - " + r_cpi.json()['description']['title'])
print(r_cpi.json()['description']['number'])

print(r_rpix.json()['description']['date'] +
      " - " + r_rpix.json()['description']['title'])
print(r_rpix.json()['description']['number'])

os.system('pause')
