import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import argparse



parser = argparse.ArgumentParser(description="download data for temp,hum etc as a csv, and plot it")
parser.add_argument('date', type=str,help="date in format dd-mm-yy")
parser.add_argument('location', type =str, help="Type name of location: kalibracja, proszkownia...")
parser.add_argument('dataType', type=str, help="what data type you need: Temperature, Humidity, Pressure, Battery")

args= parser.parse_args()


fit={
    "first" : "id",
    "sec" : "id"
}

localization = fit.get(args.location)
main_path = "main_path"

file_path = main_path+ args.date + str(localization) +".csv"


df = pd.read_csv(file_path)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.sort_values('Timestamp')

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Timestamp'], df[args.dataType])

ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.xticks(rotation=45)
plt.xlabel("Godzina")
plt.ylabel("Temperatura")
plt.title(file_path)

plt.tight_layout()
plt.show()
