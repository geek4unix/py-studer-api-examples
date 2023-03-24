import requests
import json
import hashlib
import pprint
import io
import sys

with open('creds.py') as f: exec(f.read())

# this the reference for getting SOC
info_id="7032"

errors="check creds.py and / or internet connection"

uhash = hashlib.sha256(email_address.encode('utf-8')).hexdigest()
phash = hashlib.md5(password.encode('utf-8')).hexdigest()

headers = {
"Content-Type": "text/html",
"UHASH": uhash,
"PHASH": phash
}

api_call="https://api.studer-innotec.com/api/v1/installation/synoptic/%s/?api_key=%s" % (install_id,api_key)

#keep commented unless debugging
#print (api_call)

try:
  resp = requests.get(api_call,headers=headers)
  resp_dict = resp.json()
  print(resp_dict)
except:
  print(errors)
  sys.exit(1)

try:
  request_status = pprint.pformat(resp_dict).replace("'", '"') 
  bat_soc=float(resp_dict["battery"]["soc"])
  bat_power_kw=float(resp_dict["battery"]["power"])
  bat_current=float(resp_dict["battery"]["current"])
except:
  print(errors)
  sys.exit(1)

# The API does not fail very often in terms of connection
# but it does return zero value (0) when it has no data to report
# This needs to be handled only recording data in the block below and handling any error in the if statement

if (bat_soc != 0):
  print("bat_soc: %s " % bat_soc)
else:
  print("Warn: zero reading ... skipping");
