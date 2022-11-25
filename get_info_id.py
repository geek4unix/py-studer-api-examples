import requests
import json
import hashlib
import io
import sys
import getopt

with open('creds.py') as f: exec(f.read())
def usage():
  print ("Example usage:\n\nget_info_id -i info_id 1234")

try:
  opts, args = getopt.getopt(sys.argv[1:],"i:")
except getopt.GetoptError:
   usage()
   sys.exit(2)

for opt, arg in opts:
  if not opt in ("-i"):
    usage()
    sys.exit(1)
  else:
    info_id = arg

try:
  info_id = arg
except NameError:
  usage()
  sys.exit(1)

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
  battery_soh = resp_dict['floatValue']
  print(battery_soh)
except:
  print(errors)
  sys.exit(1)

if(battery_soh=="0.0"):
  print(errors)
  sys.exit(1)
