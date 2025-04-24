# Project: CA2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#read csv file
df=pd.read_csv('CA2\Electric_Vehicle_Population_Size_History_By_County.csv')


# Exploratory Data Analysis
df.info()
df.describe()

#check for unique values in each column
print("\nUnique Values in Each Column:")
print(df.nunique())

# Data Cleaning and Preprocessing

# 1. Check and Handle Missing Values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Drop rows where County or State are missing
df = df.dropna(subset=['County', 'State'])

# Convert 'Date' to datetime format and handle errors
# Coerce invalid dates to NaT
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# Drop rows with invalid dates if needed
df = df.dropna(subset=['Date'])

# Fill missing values in 'Percent Electric Vehicles' with 0
df['Percent Electric Vehicles'] = df['Percent Electric Vehicles'].fillna(0)

# 2. Data Integrity Checks
# EV total = BEV + PHEV
ev_mismatch = df[df['Electric Vehicle (EV) Total'] != (df['Battery Electric Vehicles (BEVs)'] + df['Plug-In Hybrid Electric Vehicles (PHEVs)'])]
print(f"\nRows with EV Total mismatch: {len(ev_mismatch)}")
df = df[df['Electric Vehicle (EV) Total'] == (df['Battery Electric Vehicles (BEVs)'] + df['Plug-In Hybrid Electric Vehicles (PHEVs)'])]

# Total vehicles = EV total + non-EV
total_mismatch = df[df['Total Vehicles'] != (df['Electric Vehicle (EV) Total'] + df['Non-Electric Vehicle Total'])]
print(f"Rows with Total Vehicle mismatch: {len(total_mismatch)}")
df = df[df['Total Vehicles'] == (df['Electric Vehicle (EV) Total'] + df['Non-Electric Vehicle Total'])]

# 3. Standardize Categorical Values
df['State'] = df['State'].str.upper().str.strip()
df['County'] = df['County'].str.title().str.strip()
df['Vehicle Primary Use'] = df['Vehicle Primary Use'].str.title().str.strip()

# 4. Remove Duplicates
duplicates_count = df.duplicated().sum()
print(f"\nDuplicate Records Found: {duplicates_count}")
if duplicates_count > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")

# 5. Outlier Detection using IQR (optional: removal step)
numeric_cols = [
    'Battery Electric Vehicles (BEVs)',
    'Plug-In Hybrid Electric Vehicles (PHEVs)',
    'Electric Vehicle (EV) Total',
    'Non-Electric Vehicle Total',
    'Total Vehicles',
    'Percent Electric Vehicles'
]

def count_outliers_iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return ((series < lower) | (series > upper)).sum()

print("\n--- Outlier Count using IQR ---")
for col in numeric_cols:
    outliers = count_outliers_iqr(df[col])
    print(f"{col}: {outliers} outliers")

# Objective 1: EV Growth Over Time
df_monthly = df.groupby(df['Date'].dt.to_period('M'))['Electric Vehicle (EV) Total'].sum().reset_index()
df_monthly['Date'] = df_monthly['Date'].dt.to_timestamp()

plt.figure(figsize=(12,6))
sns.lineplot(data=df_monthly, x='Date', y='Electric Vehicle (EV) Total')
plt.title("EV Growth Trend Over Time")
plt.xlabel("Date")
plt.ylabel("EV Total")
plt.grid(True)
plt.tight_layout()
plt.show()

# Objective 2: EV Adoption by County & State

top_counties = df.groupby('County')['Percent Electric Vehicles'].mean().sort_values(ascending=False).head(10)
top_states = df.groupby('State')['Percent Electric Vehicles'].mean().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(1, 2, figsize=(16,6))
sns.barplot(x=top_counties.values, y=top_counties.index, ax=ax[0])
ax[0].set_title("Top 10 Counties by Avg % EVs")
sns.barplot(x=top_states.values, y=top_states.index, ax=ax[1])
ax[1].set_title("Top 10 States by Avg % EVs")
plt.tight_layout()
plt.show()

# Objective 3: Correlation Between BEV, PHEV, EV Total
plt.figure(figsize=(8,6))
corr = df[['Battery Electric Vehicles (BEVs)', 'Plug-In Hybrid Electric Vehicles (PHEVs)', 'Electric Vehicle (EV) Total']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Between BEV, PHEV, EV Total")
plt.tight_layout()
plt.show()

# Objective 4: Boxplot Outlier Visualization for Percent Electric Vehicles
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Percent Electric Vehicles'], color='skyblue')
plt.title("Boxplot of Percent Electric Vehicles")
plt.xlabel("Percent Electric Vehicles")
plt.tight_layout()
plt.show()


# Objective 5: Counties with 100% EVs
top_ev_counties = df[df['Percent Electric Vehicles'] == 100]['County'].value_counts().head(10)
#fig
plt.figure(figsize=(10,6))
sns.barplot(x=top_ev_counties.values, y=top_ev_counties.index, palette='Greens',)
plt.title("Top Counties with 100% EV Concentration")
plt.xlabel("Number of Records")
plt.ylabel("County")
plt.tight_layout()
plt.show()

# Objective 6: Scatter Plot - Total Vehicles vs % EVs by Usage Type
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Total Vehicles', y='Percent Electric Vehicles', hue='Vehicle Primary Use', alpha=0.6)
plt.title("EV Adoption by Vehicle Use Type")
plt.xlabel("Total Vehicles")
plt.ylabel("Percent Electric Vehicles")
plt.grid(True)
plt.legend(title='Vehicle Use')
plt.tight_layout()
plt.show()

# git
# git - man
# git - sak
# git - ary
# git-clone - https://github.com/abheeshakespeare/Python-Project---ElectroTrend.git
# git-change - ujj
# git-change - pri
# END
