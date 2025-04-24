# Electric Vehicle (EV) Population Analysis

## Project Overview
This project analyzes electric vehicle population size history data by county to track EV adoption trends, regional differences, and relationship patterns between different vehicle categories. The analysis provides insights into the growth and distribution of electric vehicles across different counties and states.

## Technologies Used
- **Python 3.x** - Core programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Seaborn** - Enhanced data visualization
- **NumPy** - Numerical operations

## Dataset
The analysis uses the "Electric_Vehicle_Population_Size_History_By_County.csv" dataset, which contains historical data on electric vehicle populations across different counties and states. The dataset includes information on:

- Battery Electric Vehicles (BEVs)
- Plug-In Hybrid Electric Vehicles (PHEVs)
- Total Electric Vehicles
- Non-Electric Vehicles
- Total Vehicles
- Electric Vehicle Percentage
- Geographic information (County, State)
- Date information
- Vehicle primary use types

## Methodology

### Data Preprocessing
The project includes comprehensive data preprocessing steps:

1. **Data Exploration** - Initial examination of data structure, statistics, and unique values
2. **Missing Value Handling** - Removing records with missing critical information (County, State, Date)
3. **Data Integrity Checks** - Verifying mathematical relationships (EV Total = BEVs + PHEVs, etc.)
4. **Data Standardization** - Normalizing categorical values (state names, county names)
5. **Duplicate Removal** - Identifying and removing duplicate records
6. **Outlier Detection** - Using IQR method to identify potential outliers in numeric columns

### Analysis Objectives

The project investigates six key objectives:

1. **EV Growth Over Time** - Tracking the trend of electric vehicle adoption over time
2. **EV Adoption by Region** - Analyzing which counties and states have the highest EV adoption rates
3. **Correlation Analysis** - Examining relationships between BEVs, PHEVs, and total EV counts
4. **Outlier Distribution** - Visualizing outliers in electric vehicle percentage
5. **100% EV Counties** - Identifying regions with complete EV adoption
6. **Vehicle Use Analysis** - Investigating the relationship between vehicle total and EV percentage by usage type

## Key Visualizations

The project produces several insightful visualizations:

1. **Line Graph** - Monthly trend of EV growth over time
 ![Screenshot 2025-04-24 205245](https://github.com/user-attachments/assets/9c3a93b1-77d1-4bcd-bcc5-44cc00059644)

2. **Bar Charts** - Top counties and states by average EV percentage
 ![Screenshot 2025-04-24 205257](https://github.com/user-attachments/assets/a42a1e54-811f-409e-9c35-486679bb4450)

3. **Correlation Heatmap** - Relationship strength between BEV, PHEV, and total EV counts
 ![Screenshot 2025-04-24 205311](https://github.com/user-attachments/assets/d2ad3488-4b5a-412e-9b25-a11e9cc59acc)

4. **Box Plot** - Distribution and outliers of EV percentage
 ![Screenshot 2025-04-24 205320](https://github.com/user-attachments/assets/d909e3cc-aafe-4dc2-b857-3e9f56238297)

5. **Bar Chart** - Counties with 100% EV concentration
 ![Screenshot 2025-04-24 205331](https://github.com/user-attachments/assets/aecbb2b1-7647-448f-a4d8-ec797245d2ea)

6. **Scatter Plot** - Relationship between total vehicles and EV percentage by primary use type
![Screenshot 2025-04-24 205342](https://github.com/user-attachments/assets/904dbb24-8a97-4c6d-ad5c-672eb9f5bde1)


## Findings and Insights

The analysis reveals:
- Temporal trends in EV adoption across the dataset period
- Geographic hotspots for electric vehicle adoption
- Strong correlations between different EV categories
- Outlier regions with unusually high or low EV percentages
- Counties with complete EV adoption
- Relationships between vehicle fleet size and electrification percentage by usage type

## Running the Project

1. Clone this repository - git clone https://github.com/Asmit03/Python-Project---ElectroTrend.git
2. Ensure you have all required libraries installed:
   ```
   pip install pandas seaborn matplotlib numpy
   ```
3. Place the "Electric_Vehicle_Population_Size_History_By_County.csv" file in the "Same" directory
4. Run the project.py script:
   ```
   python project.py
   ```

## Future Improvements
- Implement predictive modeling to forecast future EV adoption rates
- Create interactive dashboards for more dynamic exploration
- Incorporate additional datasets for deeper analysis (e.g., charging infrastructure, economic indicators)
- Perform geographic clustering analysis to identify regional patterns

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.
