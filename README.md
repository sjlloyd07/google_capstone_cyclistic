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

Moreno has set a clear goal: Design marketing strategies aimed at converting casual riders into annual members. In order to
do that, however, the marketing analyst team needs to better understand how annual members and casual riders differ, why
casual riders would buy a membership, and how digital media could affect their marketing tactics. Moreno and her team are
interested in analyzing the Cyclistic historical bike trip data to identify trends.


### ASK
#### Three questions will guide the future marketing program:
1. How do annual members and casual riders use Cyclistic bikes differently?
2. Why would casual riders buy Cyclistic annual memberships?
3. How can Cyclistic use digital media to influence casual riders to become members?

#### Stakeholders:
Lily Moreno - Director of Marketing
Cyclistic Marketing Analytics Team
Cyclistic Excecutives

#### Deliverables:
1. A clear statement of the business task
2. A description of all data sources used
3. Documentation of any cleaning or manipulation of data
4. A summary of your analysis
5. Supporting visualizations and key findings
6. Your top three recommendations based on your analysis

#### Busisness Task:
Identify how casual riders and Cyclistic members use bikes differently in order to design a strategy to convert casual riders into members.


### Prepare
The data consists of internal Cyclistic user transaction records that have had all identifying factors removed.  The dataset being used consists of monthly transaction records in the form of 13 .csv files from the months of March 2022 to March 2023 that were downloaded to local storage from the [host website](https://divvy-tripdata.s3.amazonaws.com/index.html).

The data is:
- **reliable** - consists of records from the total population that were taken using unbiased methods (timestamped transactions)
- **original** - comes from internal sources
- **comprehensive** - data metrics are accounted for an analysis focused on product use comparison between two variables (casual users/members) over a period of time
- **current** - up-to-date to the month previous to the beginning of this analysis
- **cited** - acquired using internally defined, trustworthy methods of collection

The 13 .csv files were converted into .xlsx spreadsheet files in order to use Microsoft Excel for cleaning, manipulation, analysis, and visualization of the data.  The spreadsheet files consist of raw data stored in 13 columns/fields: 
| ride_id | rideable_type	| started_at | ended_at	| start_station_name	| start_station_id	|end_station_name	| end_station_id	| start_lat	| start_lng	| end_lat	| end_lng	| member_casual |
| --- | ---	| --- | ---	| ---	| ---	| ---	| ---	| ---	| ---	| ---	| ---	| --- |
| *text* | *text*	| *datetime* | *datetime*	| *text*	| *text*	| *text*	| *text*	| *number*	| *number*	| *number*	| *number*	| *text* |

The geolocation data stored in columns *start_station_nam, start_station_id, end_station_name, end_id, start_lat, start_lng, end_lat,* and *end_lng* was determined to be too incomplete for reliable analysis.  These columns were filtered out, and the resulting dataset consisted of *ride_id, rideable_type, started_at, ended_at,* and *member_casusal*.


### Process








