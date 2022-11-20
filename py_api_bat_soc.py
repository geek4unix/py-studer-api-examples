import requests
import json
import hashlib
import io

with open('creds.py') as f: exec(f.read())

# this the reference for getting SOC
info_id="7032"


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

resp = requests.get(api_call,headers=headers)
resp_dict = resp.json()

try:
  request_status = resp_dict['status']
  battery_soc = resp_dict['floatValue']
  print(battery_soc)
except:
  print("Check creds file / connection to API")
