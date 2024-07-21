#importing the data
import pandas as pd
file_path = "/HELIO4CAST_ICMECAT_v22.csv"
df = pd.read_csv(file_path)
df.head() #Prints the head row i.e gives the list of all the features

#Taking the data of feb 2024
df['icme_start_time'] = pd.to_datetime(df['icme_start_time']) 
feb_2024_data = df[(df['icme_start_time'].dt.year == 2024) & (df['icme_start_time'].dt.month == 2)]
feb_2024_data 

#Plotting the data of feb 2024
import matplotlib.pyplot as plt

attributes = ['icme_duration', 'mo_density_mean', 'mo_temperature_mean', 'sheath_speed_mean']
attribute_labels = ['Duration (days)', 'Mean Mo Density (cm^-3)', 'Mean Mo Temperature (K)', 'Mean Sheath Speed (km/s)']

fig, axes =  plt.subplots(len(attributes), 1, figsize=(10,15), sharex=True)

for i, attribute in enumerate(attributes):
    axes[i].plot(feb_2024_data['icme_start_time'], feb_2024_data[attribute])
    axes[i].set_ylabel(attribute_labels[i])
    axes[i].grid(True)

axes[-1].set_xlabel('ICME Start Time')

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
