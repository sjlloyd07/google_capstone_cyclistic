#! python
# capstone_scrape.py - download all zip files from given host site

import os, requests, time, zipfile 
# os for filenames
# requests for downloading Response objects
# time for delay
# zipfile to manipulate zip files

from selenium import webdriver # webdriver to navigate to page objects
 


# file location url
url = "https://divvy-tripdata.s3.amazonaws.com/index.html"

# save destination folder

folder = r'C:\Users\steve\OneDrive\Desktop\Google Data Analytics\Capstone\Track 1\zipfiles'
os.makedirs(folder)
# visually inspect page and determine download elements
# desired result from trial and error: ('css selector', 'td a') contains filenames & links

# custom TestBot firefox profile has ghostery and ublockOrigin
# profile = webdriver.FirefoxProfile(r'C:\Users\steve\AppData\Roaming\Mozilla\Firefox\Profiles\snws8jty.TestBot')

#navigate to website using custom firefox profile
#driver = webdriver.Firefox(profile)
driver = webdriver.Firefox()
driver.get(url)
time.sleep(1) #allow page time to load

# create list of selenium web elements that contain file download links and filenames (all zipfiles)
web_elem_lst = driver.find_elements('css selector', 'td a')

# loop through length of list
for i in range(len(web_elem_lst)): 
    # get Response object for each webelement
    res = requests.get(web_elem_lst[i].get_attribute('href'))
    res.raise_for_status
    # download each Response object content (download items = .zipfiles)
    with open(os.path.join(folder, web_elem_lst[i].text), 'wb') as file:
        file.write(res.content)
    
        time.sleep(2) #time to download each file




### not working yet

# local zip file destination folder

# csv_datafiles = r'C:\Users\steve\OneDrive\Desktop\Google Data Analytics\Capstone\Track 1\zipfiles\unzipped'
# os.makedirs(csv_datafiles)

# # unzip files to destination
# for zip in os.listdir(folder):
#     if zipfile.is_zipfile(zip):
#         if zip[:4] == '2022' or zip[:4] == '2023': 
#             zipfile.ZipFile(os.path.join(folder, zip)).extractall(csv_datafiles)
#         continue

