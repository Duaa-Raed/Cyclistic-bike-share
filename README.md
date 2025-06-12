# Cyclistic-bike-share Case Study
 
By: Duaa Raed

**Business Task**

The goal of this case study is to analyze how annual members and casual riders use Cyclistic bikes differently, in order to help the marketing team design strategies to convert more casual riders into annual members.

**Data Source**

Data was obtained from Divvy’s public bike-share datasets provided by the City of Chicago, covering a full year (January–December 2023).

**Tools Used**

•	Python (pandas) for data cleaning and exploration

•	Power BI for data visualization and dashboard creation

**Data Cleaning and Processing**

•	Merged 12 CSV files into one dataset (over 6.8 million rows)
```python
all_files = glob.glob(path + "/*.csv")

print(f" عدد ملفات CSV: {len(all_files)}")

#  قراءة ودمج الملفات في DataFrame واحد
list_df = []
for file in all_files:
    print(f" جاري قراءة: {file}")
    df = pd.read_csv(file)
    list_df.append(df)

merged_df = pd.concat(list_df, ignore_index=True)
 ```


•	Converted date/time fields to proper datetime format
```python
date_cols = ['started_at', 'ended_at']

for col in date_cols:
    merged_df[col] = pd.to_datetime(merged_df[col], errors='coerce')
 ```

•	Calculated new fields: ride_length, day_of_week, month
```python
merged_df['hour'] = merged_df['started_at'].dt.hour
merged_df['month'] = merged_df['started_at'].dt.month_name()
merged_df['day_of_week'] = merged_df['started_at'].dt.day_name()
merged_df['quarter'] = merged_df['started_at'].dt.quarter.map({1: 'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4'})
```

•	To enable time-based analysis, ride hours were categorized into periods of the day (Morning, Afternoon, Evening, Night) based on the start hour of each ride.
```python

def get_day_period(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

merged_df['day_period'] = merged_df['hour'].apply(get_day_period)
merged_df.info()
```

•	Ensured clean and reliable data for analysis

**Analysis Highlights**

•	 Total Trips reached 6 million rides in 2023, indicating a strong demand for bike-share services throughout the year.

•	 Electric bikes were the most preferred type, showing users inclination toward faster and more convenient transportation.

•	 Members accounted for the majority of rides **(64%)**, suggesting strong retention and engagement among subscribers.

•	 Peak usage hour was at **17:00 (5 PM)**, aligning with the end of typical work hours and commute patterns.

•	 Saturday was the busiest day of the week, showing that weekends attract the highest ridership.

•	 August had the highest number of rides, indicating that summer is the peak season for bike-sharing activities.

These trends highlight both commuter behavior and seasonal demand, which can help optimize fleet distribution, membership campaigns, and maintenance scheduling.

**Visuals used in the Power BI dashboard:**

•	Card Visuals :

•	Used to display key performance indicators (KPIs) such as:

•	Total Trips

•	Top Bike Type

•	Top Rider Type

•	Peak Hour

•	Top Day

•	Top Month

•	Stacked Column Chart :

•	Visualizes the monthly and quarterly ride distribution.

•	Shows ride volume for both casual and member users per month.

•	Bar Chart :

•	Compares rider types (casual/member) across different bike types.

•	Line Chart :

•	Displays rides by hour, split by rider type to identify peak usage hours.

•	Donut Chart :

•	Shows the proportion of rides between casual and member users.

•	Clustered Column Chart :

•	Visualizes rides by day of the week for both casual and member users.

**Recommendations**

Based on the analysis of Cyclicity’s rider behaviors and usage patterns, the following recommendations are proposed:

•	Encourage Casual Riders to Become Members

Casual riders contribute significantly during weekends and peak hours. Offering targeted membership promotions, such as weekend discounts or free trials, could help convert them into long-term members.

•	Focus on Peak Hours for Promotions

The majority of trips occur between *5 PM and 6 PM*, indicating strong after-work usage. Marketing campaigns or app-based incentives during these hours could boost engagement.

•	Optimize Bike Distribution During Popular Times

The highest activity occurs in July and on Saturdays, especially in Quarter 3. Bike rebalancing efforts should be increased during these peak times to avoid shortages.

•	Increase Bike Availability for Most Popular Bike Types

The most used bike type is *electric_bike*. Ensuring sufficient availability and maintenance of this type will improve customer satisfaction.

•	Enhance User Experience Through App Insights

Utilize app notifications and ride history insights to remind users of optimal times to ride or membership benefits, based on their past behaviors.

