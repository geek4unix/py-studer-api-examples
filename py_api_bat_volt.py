import requests
import json
import hashlib
import io
import sys

with open('creds.py') as f: exec(f.read())

# this the reference for getting SOC
info_id="3092"

errors="check creds.py and / or internet connection"

uhash = hashlib.sha256(email_address.encode('utf-8')).hexdigest()
phash = hashlib.md5(password.encode('utf-8')).hexdigest()

headers = {
"Content-Type": "text/html",
"UHASH": uhash,
"PHASH": phash
}

api_call="https://api.studer-innotec.com/api/v1/installation/user-info/%s?device=XT_Group&infoId=%s&api_key=%s" % (install_id,info_id,api_key)

#keep commented unless debugging
#print (api_call)
try:
  resp = requests.get(api_call,headers=headers)
  resp_dict = resp.json()
except:
  print(errors)
  sys.exit(1)
try:
  request_status = resp_dict['status']
  battery_volt = resp_dict['floatValue']
  print(battery_volt)
except:
  print(errors)
  sys.exit(1)

if(battery_volt=="0.0"):
  print(errors)
  sys.exit(1)
