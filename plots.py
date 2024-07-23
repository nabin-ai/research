import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'HELIO4CAST_ICMECAT_v22.csv'
data = pd.read_csv(file_path)

# Convert the icme_start_time column to datetime format
data['icme_start_time'] = pd.to_datetime(data['icme_start_time'])

# Filter the data for events that occurred in February 2024
february_2024_data = data[(data['icme_start_time'].dt.year == 2024) & (data['icme_start_time'].dt.month == 2)]

# Define the attributes to plot against icme_start_time
attributes = ['icme_duration', 'mo_density_mean', 'mo_temperature_mean', 'sheath_speed_mean']
attribute_labels = ['ICME Duration (hours)', 'MO Density Mean (cm^-3)', 'MO Temperature Mean (K)', 'Sheath Speed Mean (km/s)']

# Define a color palette for the plots
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
markers = ['o', 's', 'D', '^']

# Create a figure with multiple subplots
fig, axes = plt.subplots(len(attributes), 1, figsize=(12, 18), sharex=True)

# Plot each attribute against icme_start_time with enhancements
for i, attribute in enumerate(attributes):
    axes[i].plot(february_2024_data['icme_start_time'], february_2024_data[attribute],
                 color=colors[i], marker=markers[i], linestyle='-', markersize=8, linewidth=2, label=attribute_labels[i])
    axes[i].set_ylabel(attribute_labels[i], fontsize=12)
    axes[i].set_title(f'{attribute_labels[i]} vs ICME Start Time', fontsize=14)
    axes[i].legend(loc='best')
    axes[i].grid(True, linestyle='--', alpha=0.6)

# Set the x-axis label
axes[-1].set_xlabel('ICME Start Time', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout for better spacing
plt.tight_layout()

# Save the figure to a file
output_file_path = 'icme_february_2024_plots.png'
fig.savefig(output_file_path)

output_file_path

# Provide a link to download the file
from google.colab import files
files.download(output_file_path)
