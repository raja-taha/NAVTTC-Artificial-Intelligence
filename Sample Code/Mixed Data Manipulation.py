import pandas as pd
import numpy as np

# Example DataFrame
data = {
    'mixed_column': [10, 20, 'a', 30, 'b', 40]
}
df = pd.DataFrame(data)

# Filter out non-numeric values
numeric_values = pd.to_numeric(df['mixed_column'], errors='coerce')

# Calculate the mean of numeric values
mean_value = numeric_values.mean()

print(f'The mean of the numeric values is: {mean_value}')
