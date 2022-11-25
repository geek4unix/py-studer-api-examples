## py-studer-api-examples

Some sample python scripts to get information about power devices from Studer Innotec API service.


#Setup
--

*MODIFY creds.py file

*RUN python command

#Examples
--

**General Get info command**

Retrieve the value for the parameter specified as -i XXXX where XXXX is an property/info id

> python3.10  get_info_id.py -i 7032
> Return value: 89


**Get battery SOC from XTM device Command**

> python3.10 py_api_bat_soc.py
> Return value: 82.0

**Get battery voltage from XTM device Command**

> python3.10 py_api_bat_volt.py          
> Return value: 49.59375

--

[Studer-Innotec API Swagger Docs](https://api.studer-innotec.com/swagger/ui/index)
