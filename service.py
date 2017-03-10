# -*- coding: utf-8 -*-
import urllib2, json, csv, boto3

s3 = boto3.resource('s3')

def handler(event, context):
  api_key = event['params']['querystring']['api_key']
  date_range = event['params']['querystring']['date_range']
  json_string = urllib2.urlopen("https://openexchangerates.org/api/latest.json?app_id=%s" % api_key).read()
  json_data = json.loads(json_string)

  csv_string = 'country,rate'
  for k, v in json_data['rates'].items():
    csv_string = csv_string + "\n{},{}".format(k, v)

  return {'csv': csv_string}