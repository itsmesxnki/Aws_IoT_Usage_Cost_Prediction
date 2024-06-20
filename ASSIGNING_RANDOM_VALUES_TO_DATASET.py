import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv(r"C:\Users\monis\Downloads\Duplicated_Billing_Data_1 copy.csv", sep=',')

# Convert columns to numeric type
df['UsageQuantity'] = pd.to_numeric(df['UsageQuantity'])
df['CostBeforeTax'] = pd.to_numeric(df['CostBeforeTax'])
df['TaxAmount'] = pd.to_numeric(df['TaxAmount'])

# Randomize 'UsageQuantity', 'CostBeforeTax', and 'TaxAmount' columns
df['UsageQuantity'] = np.random.randint(1, 10, df.shape[0])
df['CostBeforeTax'] = np.random.randint(10, 16, df.shape[0])
df['TaxAmount'] = np.random.randint(1, 6, df.shape[0])

# Write the DataFrame to a new CSV file
df.to_csv(r"C:\Users\monis\Downloads\Duplicated_Billing_Data_1_randomized.csv", sep=',', index=False)