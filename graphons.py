import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

r_rpi = requests.get(
    "https://api.ons.gov.uk/dataset/mm23/timeseries/CHAW/data")
r_cpi = requests.get(
    "https://api.ons.gov.uk/dataset/mm23/timeseries/D7BT/data")
r_rpix = requests.get(
    "https://api.ons.gov.uk/dataset/mm23/timeseries/CHMK/data")

# df = pd.Dataframe({'RPI': [], 'RPIX': [], 'CPI': []})
month_to_num = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
                'June': 6, 'July': 7, 'August': 8, 'September': 9,
                'October': 10, 'November': 11, 'December': 12}

rpi = {}
rpix = {}
cpi = {}

d_rpi = {}
d_rpix = {}
d_cpi = {}

for month in r_rpi.json()['months']:
    rpi[(month['year'], month['month'])] = float(month['value'])
    last_year = str(int(month['year']) - 1)
    if (last_year, month['month']) in rpi:
        date = pd.datetime(int(month['year']),
                           month_to_num[month['month']], 1)
        d_rpi[date] = ((float(month['value']) /
                        rpi[(last_year, month['month'])]) - 1) * 100

for month in r_rpix.json()['months']:
    rpix[(month['year'], month['month'])] = float(month['value'])
    last_year = str(int(month['year']) - 1)
    if (last_year, month['month']) in rpix:
        date = pd.datetime(int(month['year']),
                           month_to_num[month['month']], 1)
        d_rpix[date] = ((float(
            month['value']) / rpix[(last_year, month['month'])]) - 1) * 100

for month in r_cpi.json()['months']:
    cpi[(month['year'], month['month'])] = float(month['value'])
    last_year = str(int(month['year']) - 1)
    if (last_year, month['month']) in cpi:
        date = pd.datetime(int(month['year']),
                           month_to_num[month['month']], 1)
        d_cpi[date] = ((float(
            month['value']) / cpi[(last_year, month['month'])]) - 1) * 100

inflation = pd.DataFrame({'RPI': pd.Series(d_rpi),
                          'RPIX': pd.Series(d_rpix),
                          'CPI': pd.Series(d_cpi)})

sns.set_style("white")
g = sns.relplot(kind='line', data=inflation, palette='colorblind')
sns.despine(left=True)
g.fig.autofmt_xdate()

g.ax.yaxis.grid(True)

plt.xticks(rotation=90)

plt.show()

# os.system('pause')
