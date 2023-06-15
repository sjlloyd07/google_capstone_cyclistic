# Cyclistic
## Case Study: How does a bike-share navigate speedy success?

### Company
  In 2016, Cyclistic launched a successful bike-share offering. Since then, the program has grown to a fleet of 5,824 bicycles that
are geotracked and locked into a network of 692 stations across Chicago. The bikes can be unlocked from one station and
returned to any other station in the system anytime.

  Until now, Cyclistic’s marketing strategy relied on building general awareness and appealing to broad consumer segments.
One approach that helped make these things possible was the flexibility of its pricing plans: single-ride passes, full-day passes,
and annual memberships. Customers who purchase single-ride or full-day passes are referred to as casual riders. Customers
who purchase annual memberships are Cyclistic members.

Cyclistic’s finance analysts have concluded that annual members are much more profitable than casual riders. Although the
pricing flexibility helps Cyclistic attract more customers, Moreno believes that maximizing the number of annual members will
be key to future growth. Rather than creating a marketing campaign that targets all-new customers, Moreno believes there is a
very good chance to convert casual riders into members. She notes that casual riders are already aware of the Cyclistic
program and have chosen Cyclistic for their mobility needs.

**Moreno has set a clear goal:** Design marketing strategies aimed at converting casual riders into annual members. In order to
do that, however, the marketing analyst team needs to better understand how annual members and casual riders differ, why
casual riders would buy a membership, and how digital media could affect their marketing tactics. Moreno and her team are
interested in analyzing the Cyclistic historical bike trip data to identify trends.

### Assignment Details
#### Three questions will guide the future marketing program:
1. How do annual members and casual riders use Cyclistic bikes differently?
2. Why would casual riders buy Cyclistic annual memberships?
3. How can Cyclistic use digital media to influence casual riders to become members?

#### Stakeholders:
- Lily Moreno - Director of Marketing
- Cyclistic Marketing Analytics Team
- Cyclistic Excecutives

#### Report Prompt: *How do annual members and casual riders use Cyclistic bikes differently?*

#### Report Deliverables:
1. A clear statement of the business task
2. A description of all data sources used
3. Documentation of any cleaning or manipulation of data
4. A summary of your analysis
5. Supporting visualizations and key findings
6. Your top three recommendations based on your analysis

### ASK
**Problem:** A large percentage of Cyclistic users are casual riders.  The executive team wants to convert casual riders into members.
**Goal:** Identify how casaul riders and members use Cyclistic products.  How customers use Cyclstic products includes date/time of use, duration, product type, and location.

**Questions to Answer:** 
- *When* do they use the product? 
- *How long* do they use the product? 
- *Which product* do they use? 
- *Where* do they use the product?

#### Busisness Task:
Identify trends of how casual riders and Cyclistic members used bikes over the previous year and present a visualization of the comparison clearly for stakeholders.


### Prepare
The data consists of internal Cyclistic user transaction records that have had all identifying factors removed.  The datasets being used consist of monthly transaction records in the form of 13 .csv files from the months of March 2022 to March 2023 that were downloaded to local storage from the [host website](https://divvy-tripdata.s3.amazonaws.com/index.html) using a python script found [here](capstone_scrape.py).  Each data file was then unzipped and consolidated into one folder.  One at a time, each .csv file was loaded into Excel with Power Query for initial evaluation. 

Each .csv file contained raw data stored in 13 fields formatted below as detected by Power Query: 
| ride_id | rideable_type	| started_at | ended_at	| start_station_name	| start_station_id	|end_station_name	| end_station_id	| start_lat	| start_lng	| end_lat	| end_lng	| member_casual |
| --- | ---	| --- | ---	| ---	| ---	| ---	| ---	| ---	| ---	| ---	| ---	| --- |
| *text* | *text*	| *datetime* | *datetime*	| *text*	| *text*	| *text*	| *text*	| *decimal number*	| *decimal number*	| *decimal number*	| *decimal number*	| *decimal text* |

The field ***ride_id*** contains unique values and is the primary key of each dataset.

The data was transormed in Power Query to filter out the following fields that contained values irrelevant for this analysis: 
| start_station_id	| end_station_id	| start_lat	| start_lng	| end_lat	| end_lng	|
| ---	| ---	| ---	| ---	| --- | --- |

The remaining data fields below were then ready for further cleaning and manipulation.
| ride_id | rideable_type	| started_at | ended_at	| start_station_name	| end_station_name	| member_casual |
| --- | ---	| --- | ---	| ---	| ---	| ---	|

The data is:
- **reliable** - consists of records from the total population that were taken using unbiased methods (non-identifying timestamped transactions)
- **original** - comes from internal Cyclistic sources
- **comprehensive** - data contains all relevant metrics required for intended analysis focused on product use comparison between two variables (casual users/members) over a period of time
- **current** - up-to-date to the month previous to the beginning of this analysis
- **cited** - acquired using internally defined, trustworthy methods of collection

### Process
The Microsoft Power Query Editor was used to further transform the raw dataset into a spreadsheet ready for analysis.  After filtering out the initially identified unneccessary fields, the columns containing the calculated values below were added using tools in the "Add Column" tab in ordered to get the desired metrics from the data.

| field | description | 
| --- | ---	| 
| ride_length | "Custom Column" tool used to input a formula to calculate length of ride (in minutes) (=*ended_at - started_at*) | 
| hour_of_day | "Time" tool used to extract start of hour values from selected *started_at* field |
| date | "Date" tool used to extract the short date from selected *started_at* field | 

Fields *started_at* and *ended_at* were no longer necessary and removed from the query using the "Choose Columns" tool.


The resulting 8 fields were then loaded into the spreadsheet as columns ordered below:
| ride_id | rideable_type	| date | hour_of_day | ride_length	| start_station_name	| end_station_name	| member_casual |
| --- | ---	| --- | ---	| ---	| ---	| ---	| ---	|

| day_of_week | day of week number extracted from *started_at* using (=*WEEKDAY()*)	| 

This process was applied identically to every dataset by copying the code from the first Power Query Advanced Editor and pasting it into every subsequently loaded dataset Power Query Editor Advanced Editor and changing the source filename before proceeding.

#### Cleaning

Once the datasets were in spreadsheet form, they were checked for duplicate records w/ the *remove duplicates* Excel feature (no duplicates found).  Further visual exmamination and the filtering tool were performed on each column to confirm all cells had consistent formatting and conforming values.

***ride_id***
- appeared to be unique 16 character alphanumeric values
-	column filter and sort features were used to inspect that all column values conform to the same standard
-	inserted new *check* column to the right of *ride_id* for further value checking
-	confirmed all *ride_id* cells had character lengths of 16 using the *=len()* function and filter
  - one dataset was found to contain non-conforming values stored in "text" format incorrectly representing scientific notation values
  - Further investigation revealed 169 *ride_id* values w/ non-conforming characteristics stored incorrectly in the raw data for March 2023 (filename: 202303-divvy-tripset).  Without a way to correct these records, they were deleted from the dataset.
-	*check* column was deleted after all datasets were checked

*rideable_type, member_casusal*
- expected, conforming values

*date*
- short date format

*hour_of_day*
- date/time format

*ride_length*
- time format 37:30:55 (hh:mm:ss)
- invalid values (impossible calculations) were found and removed from the files below

| filename | records deleted | 
| --- | ---	| 
| 202203-divvy-tripdata | 2 |
| 202205-divvy-tripdata | 1 |
| 202206-divvy-tripdata | 12 |
| 202207-divvy-tripdata | 16 |
| 202208-divvy-tripdata | 15 |
| 202209-divvy-tripdata | 9 |
| 202210-divvy-tripdata | 4 |
| 202211-divvy-tripdata | 41 |
| 202302-divvy-tripdata | 2 |


#### Manipulation

After cleaning, another calculated row was added that could not be reasonably done in the Power Query Editory.

| field | description | 
| --- | ---	| 
| day_of_week | calculated the weekday number from each *started_at* value using the *=WEEKDAY()* function, format as "general" | 

After the new column was added, the newly calculated column containing formulas was replaced w/ the calculated values they contained using *Copy / Paste Values*.

The final spreadsheets ready for consolidation and analysis contain the columns below:
| ride_id | rideable_type	| date | day_of_week | hour_of_day | ride_length	| start_station_name	| end_station_name	| member_casual |
| --- | ---	| --- | ---	| ---	| ---	| ---	| ---	| ---	|



### Analysis

Power Query was used to consolidate the data into a pivot table.  The analysis was focused on the Cyclistic ride user status variable of which two values were compared - *member* and *casual* - and was performed on the final dataset that contained **6,087,365** records that were taken between **March 2022** and **March 2023**.

#### Frequency
Cyclistic members (member) took 20% more rides over the time period than Cyclistic casual riders (casual).

![image](https://github.com/sjlloyd07/google_capstone_cyclistic/assets/97957522/8d515013-973d-4ac4-93e9-abac8f59c603)

Members took more rides than casual in every month of the year.  Rides taken by both groups followed a similar trend over the year with the fewest number of rides taken during the winter months and a gradual increase through the spring and peaking in the summer months.  The smallest difference between total rides of both groups was in July - less than 2%, and the greatest difference - almost 60% - was in January.

![image](https://github.com/sjlloyd07/google_capstone_cyclistic/assets/97957522/ec0acbf7-378d-4d34-b2ac-0809aa9889fa)

Members and casuals had the least difference in total rides taken over the weekend - less than 2% - and Sunday is the only day of the week that casuals had more rides than members.  Throughout the week, rides taken by both groups had an inverse relationship with member rides increasing and peaking in the middle of the week and casual rides declining to the lowest levels during the same time period.

![image](https://github.com/sjlloyd07/google_capstone_cyclistic/assets/97957522/2dbcbc08-ca51-4491-ba25-d22c088216fc)


Members and casuals followed a slightly difference trend in an average 24 hour day.  Casual total rides increased gradually through the morning hours and peaked at 5 pm.  Member rides also peaked at 5 pm, but a ride spike was also observed at 8 am before dropping and increasing again in the afternoon.

![image](https://github.com/sjlloyd07/google_capstone_cyclistic/assets/97957522/4bab800f-6141-4132-8327-3ab1a0588e97)



