import requests
from bs4 import BeautifulSoup
import csv
import datetime

fund_details = []

request_urls = [
  'https://www.moneycontrol.com/mutual-funds/nav/quant-active-fund-direct-plan/MES061',
  'https://www.moneycontrol.com/mutual-funds/nav/hdfc-index-fund-direct-plan-nifty-50-plan/MHD1152',
  'https://www.moneycontrol.com/mutual-funds/nav/tata-index-fund-nifty-plan-direct-plan/MTA763',
]

for req_url in request_urls:
  res = requests.get(req_url)
  res_text = res.text
  res_status = res.status_code

  soup = BeautifulSoup(res.content, 'html.parser')
  page_title = soup.title.text
  all_headers = []


  for element in soup.select('h1'):
    all_headers.append(element.text)

  percent_change = ''
  if (len(soup.select('span.green_text'))): 
    percent_change = '+' + soup.select('span.green_text')[0].text
  elif (len(soup.select('span.red_text'))):
    percent_change = soup.select('span.red_text')[0].text
  
  fund_details.append({
    'fund_name': all_headers[0],
    'latest_nav': soup.select('span.amt')[0].text,
    'percent_change': percent_change,
    'link': req_url,
    'nav_date': soup.select('div.grayvalue')[0].text,
    'time': str(datetime.datetime.now()),
  })

file_headers = fund_details[0].keys()

with open('/home/harsh/drive/projects/mf-details-scrapper/mf_details.csv', 'w',newline='') as output_file:
  writer = csv.DictWriter(output_file, file_headers)
  writer.writeheader()
  writer.writerows(fund_details)
