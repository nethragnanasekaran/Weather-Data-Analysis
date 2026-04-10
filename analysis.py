import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/weather.csv')

print("Dataset Preview:")
print(df.head())

plt.figure()
plt.plot(df['Day'], df['Temperature'])
plt.title('Temperature Trend')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.savefig('../images/temperature_trend.png')
plt.show()

plt.figure()
plt.bar(df['Day'], df['Rainfall'])
plt.title('Rainfall Analysis')
plt.xlabel('Day')
plt.ylabel('Rainfall')
plt.savefig('../images/rainfall_chart.png')
plt.show()

plt.figure()
plt.plot(df['Day'], df['Humidity'])
plt.title('Humidity Trend')
plt.xlabel('Day')
plt.ylabel('Humidity')
plt.savefig('../images/humidity_trend.png')
plt.show()

print("Highest Temperature:", df['Temperature'].max())
print("Highest Rainfall:", df['Rainfall'].max())
