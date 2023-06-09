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
The data consists of internal Cyclistic user transaction records that have had all identifying factors removed.  The datasets being used consist of monthly transaction records in the form of 13 .csv files from the months of March 2022 to March 2023 that were downloaded to local storage from the [host website](https://divvy-tripdata.s3.amazonaws.com/index.html).

The data is:
- **reliable** - consists of records from the total population that were taken using unbiased methods (non-identifying timestamped transactions)
- **original** - comes from internal Cyclistic sources
- **comprehensive** - data contains all relevant metrics required for intended analysis focused on product use comparison between two variables (casual users/members) over a period of time
- **current** - up-to-date to the month previous to the beginning of this analysis
- **cited** - acquired using internally defined, trustworthy methods of collection

The 13 .csv files were converted into .xlsx spreadsheet files in order to use Microsoft Excel for cleaning, manipulation, analysis, and visualization of the data.  The spreadsheet files contain raw data stored in 13 columns/fields: 
| ride_id | rideable_type	| started_at | ended_at	| start_station_name	| start_station_id	|end_station_name	| end_station_id	| start_lat	| start_lng	| end_lat	| end_lng	| member_casual |
| --- | ---	| --- | ---	| ---	| ---	| ---	| ---	| ---	| ---	| ---	| ---	| --- |
| *text* | *text*	| *datetime* | *datetime*	| *text*	| *text*	| *text*	| *text*	| *number*	| *number*	| *number*	| *number*	| *text* |

Initial evaluation of the data showed that the location data fields were missing values.  Records containing missing values accounted for up to 20% of the dataset and removing them may have significant impact on analysis results.  At this time, location data will not be evaluated in this analysis.  The following analysis focuses on customer product type use and time periods of use.

The geolocation data stored in columns *start_station_nam, start_station_id, end_station_name, end_id, start_lat, start_lng, end_lat,* and *end_lng* was determined to be too incomplete for reliable analysis.  These columns were filtered out, and the resulting dataset consisted of *ride_id, rideable_type, started_at, ended_at,* and *member_casusal*.


### Process
Microsoft Excel was used to clean and manipulate the data.  For every dataset spreadsheet, the sheet containing raw data was copied to a new sheet in the workbook for cleaning/manipulation in order to leave the raw data intact.  The following actions were performed on each spreadsheet of the dataset.

#### Cleaning

Visual exmamination and the value filtering function were performed on each column to confirm all formatting was consistent and conforming.

***ride_id***
- field contains unique values (primary key of dataset)
- values are a mix of alphanumeric general formatting and scientific notation numbers of different lengths
- the nonconforming scientific notation values were imputed as unreliable and deleted w/o significant statistical effects
  - new *check column* inserted next to *ride_id* for *ride_id* value calculations
  - all *ride_id* values were check for formatting w/ the *=istext()* function
  - the *check* column was filtered to show check values that returned FALSE (*ride_id* contained non-conforming numeric data) and deleted
- the *check* column values were then changed to check the character length of each *ride_id* values using the *=len()* function (16 character length is conforming)
- the results showed all remainging *ride_id* values conformed

| filename | non-conforming records deleted	|
| --- | ---	|
| 202203-divvy-tripdata-clean | 190 |
| 202204-divvy-tripdata-clean | 249 |
| 202205-divvy-tripdata-clean	| 412 |
| 202206-divvy-tripdata-clean	| 512 |
| 202207-divvy-tripdata-clean	| 543 |
| 202208-divvy-tripdata-clean	| 529 |
| 202209-divvy-tripdata-clean	| 463 |
| 202210-divvy-tripdata-clean	| 404 |
| 202211-divvy-tripdata-clean	| 216 |
| 202212-divvy-tripdata-clean	| 119 |
| 202301-divvy-tripdata-clean	| 127 |
| 202302-divvy-tripdata-clean	| 140 |
| 202303-divvy-tripdata-clean	| 169 |

*rideable_type, member_casusal*
- expected and confirmed to correctly be *text* formatted

*started_at, ended_at*
- expected and confirmed to correctly be *datetime* formatted

- spreadsheet is checked for duplicate records w/ the *remove duplicates* Excel feature (no duplicates found)


#### Manipulation

In order to perform the desired analysis on the data, addtional columns containing calculated values were added to the spreadsheets.

- column *ride_length* was added that contained the calculated duration of each ride record (*= ended_at - started_at*)
  - time format hh:mm:ss
- column *day_of_week* was added to extract the weekday number from each *started_at* value using the *=WEEKDAY()* function
  - number format
- column *hour_of_day* was added to extract the time to the full hour from each *started_at* value using *=TIME(HOUR(started_at),0,0)*
  - time format HH:MM AM/PM
- column *date* was added to extract the date from each *started_at* value using *=ROUNDDOWN(started_at),0)*
  - short date format m:dd:yyyy

After all new columns were added, the newly calculated cells containing formulas were replaced w/ the calculated values they contained.


### Analysis

The datasets were consolidated into a PivotTable by using a Power Query to connect to the folder in which all the spreadsheets are located, and combining them into 





