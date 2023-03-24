# py-studer-api-examples

Some sample python scripts to get information about power devices from Studer Innotec API service.

Probably the only script you need to get most of the information you will need, in a single API call is:

py_api_syntopic.py


I've left the other scripts in the repo for reference.


Setup

-----

*MODIFY creds.py file

*RUN python command

Examples

--------
*Get syntopic command*

Retrieve a bunch of parameters in json format, with output similar to:

`% python3.10 py_api_syntopic.py

{'energy': {'hasSolar': True, 'solar': 6.51, 'yesterdaySolar': 6.02, 'solarUnit': 'kWh', 'hasInverter': True, 'gridGenset': 0.0, 'yesterdayGridGenset': 0.0, 'gridGensetUnit': 'kWh', 'load': 4.09, 'yesterdayLoad': 5.05, 'loadUnit': 'kWh', 'hasBatteryStatusProcessor': True, 'batteryCharge': 70.62, 'batteryChargeUnit': 'Ah', 'yesterdayBatteryCharge': 62.88, 'batteryDischarge': 40.12, 'batteryDischargeUnit': 'Ah', 'yesterdayBatteryDischarge': 65.56}, 'battery': {'power': -0.27, 'powerUnit': 'kW', 'voltage': 49.72, 'voltageUnit': 'V', 'current': -5.4, 'currentUnit': 'A', 'soc': 91.0, 'socUnit': '%', 'temperature': 20.3, 'temperatureUnit': '°C', 'temperatureUnitHtml': '&#176;C', 'hasBatteryStatusProcessor': True}, 'power': {'hasSolar': True, 'solar': 0.0, 'solarUnit': 'kW', 'hasInverter': True, 'gridGenset': 0.0, 'gridGensetUnit': 'kW', 'load': 0.24, 'loadUnit': 'kW', 'hasBatteryStatusProcessor': True, 'battery': -0.27, 'batteryUnit': 'kW'}}
`

*General Get info command*

Retrieve the value for the parameter specified as -i XXXX where XXXX is an property/info id

'''
python3.10  get_info_id.py -i 7032
'''

Return value: 89


*Get battery SOC from XTM device Command*	

'''
python3.10 py_api_bat_soc.py
'''

Return value: 82.0

*Get battery voltage from XTM device Command*

'''
python3.10 py_api_bat_volt.py          
'''

Return value: 49.59375

--

Studer-Innotec API Swagger Docs:

https://api.studer-innotec.com/swagger/ui/index
