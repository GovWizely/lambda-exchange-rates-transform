# -*- coding: utf-8 -*-
import urllib2, json, csv, boto3, datetime

s3 = boto3.resource('s3')
currency_codes = [
  "ARS",
  "BDT",
  "CNY",
  "COP",         
  "CZK",
  "EGP",
  "HUF",
  "IDR",
  "IRR",
  "ILS",
  "KES",
  "LVL",
  "MAD",
  "OMR",
  "PKR",
  "PHP",
  "PLN",
  "RON",
  "RUB",
  "TTD",
  "TRY",
  "UAH",
  "AED",
  "VND",
  "BGN"
]

def handler(event, context):
  api_key = event['params']['querystring']['api_key']
  start_date = datetime.datetime.strptime(event['params']['querystring']['start_date'], "%Y-%m-%d")
  end_date = datetime.datetime.strptime(event['params']['querystring']['end_date'], "%Y-%m-%d")

  data = fetch_data(start_date, end_date, api_key)
  sorted_data = sorted(data, key=lambda k: k['country'])
  csv_string = build_csv_string(sorted_data)
  print csv_string
  return {'csv': csv_string }

def reversed_daterange(start_date, end_date):
  for n in range( ( end_date - start_date ).days + 1 ):
    yield end_date - datetime.timedelta( n )

def fetch_data(start_date, end_date, api_key):
  data = []
  for date in reversed_daterange(start_date, end_date):
    date_string = date.strftime('%Y-%m-%d')
    json_string = urllib2.urlopen("https://openexchangerates.org/api/historical/{}.json?app_id={}".format(date_string, api_key)).read()
    json_data = json.loads(json_string)
    for k, v in json_data['rates'].iteritems():
      if k in currency_codes:
        data.append({'date': date.strftime('%m/%d/%Y'), 'country': k + "=", 'rate': v})
  return data

def build_csv_string(sorted_data):
  csv_string = 'RIC,Trade_Date,Bid_Price'
  for entry in sorted_data:
    csv_string = csv_string + "\n{},{},{}".format(entry['country'], entry['date'], entry['rate'])
  return csv_string
 
