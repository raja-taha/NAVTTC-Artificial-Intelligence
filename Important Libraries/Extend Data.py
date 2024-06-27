import pandas as pd
import numpy as np

# Define the possible values for each column
sky_options = ['sunny', 'rainy', 'cloudy']
air_temp_options = ['warm', 'cold', 'mild']
humidity_options = ['high', 'normal', 'low']
wind_options = ['strong', 'weak', 'moderate']
water_options = ['warm', 'cool', 'cold']
forecast_options = ['same', 'change', 'different']
enjoy_sport_options = ['yes', 'no']

# Generate random data
np.random.seed(42)  # For reproducibility
data = {
    'sky': np.random.choice(sky_options, 50),
    'airTemp': np.random.choice(air_temp_options, 50),
    'humidity': np.random.choice(humidity_options, 50),
    'wind': np.random.choice(wind_options, 50),
    'water': np.random.choice(water_options, 50),
    'forecast': np.random.choice(forecast_options, 50),
    'enjoySport': np.random.choice(enjoy_sport_options, 50)
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('../Datasets/data.csv', index=False)

print("Data saved to data.csv")