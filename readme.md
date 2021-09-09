# scrapped-mf-details
- This repo contains a python script to scrape scheme data for different mutual funds  from moneycontrol and store it in a file.

- The script runs through a cron job scheduled for 3 different time 9am, 1pm and 5pm respectively.

- The script scraps the following details - 
  - Scheme name
  - NAV
  - Percentage Change
  - Last Updated NAV date
  - Date Updation time
 
- These details are stored in a csv file.

- The scheme can also be added or removed, just have to update the request_urls with moneycontrol's url for that particular scheme in the file named run.py