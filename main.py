import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import argparse
import json

parser = argparse.ArgumentParser(description="download data for temp,hum etc as a csv, and plot it")
parser.add_argument('date', type=str,help="date in format dd-mm-yy")
parser.add_argument('location', type =str, help="Type name of location: kalibracja, proszkownia...")
parser.add_argument('dataType', type=str, help="what data type you need: Temperature, Humidity, Pressure, Battery")
parser.add_argument('anomaly', type=int, help="anomaly")

args= parser.parse_args()


with open('main/config.json') as f:
    config = json.load(f)
main_path = config['main_path']
fit = config['fit']



localization = fit.get(args.location)


#file_path = main_path+ args.date + str(localization) +".csv"
file_path = main_path+args.date+"/"+str(localization)+'.csv'

df = pd.read_csv(file_path)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.sort_values('Timestamp')



fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Timestamp'], df[args.dataType])

ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.xticks(rotation=45)
plt.xlabel("Godzina")
plt.ylabel(args.dataType)
plt.title(file_path)

stats = df[args.dataType].describe()

stat_text = (
    f"Mean: {stats['mean']:.2f}\n"
    f"Min: {stats['min']:.2f}\n"
    f"Max: {stats['max']:.2f}\n"
    f"Median: {df[args.dataType].median():.2f}\n"
    f"Std: {stats['std']:.2f}"
)

ax.text(
    0.98, 0.95, stat_text,
    transform=ax.transAxes,
    verticalalignment='top',
    horizontalalignment='right',
    bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.7),
    fontsize=9
)


threshold = args.anomaly
anomalies = df[df[args.dataType] > threshold]
plt.scatter(anomalies['Timestamp'], anomalies[args.dataType], color='red', label='Anomalie')
plt.legend()

plt.tight_layout()
plt.show()
