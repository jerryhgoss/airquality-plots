'''
    This code will be using the quant-aq docs to access sensor information from their database. The link to the API docs can be found https://docs.quant-aq.com/api. 
    
    https://api.quant-aq.com/device-api/v1/account <<< This is the api structure to call your account information
    
    https://api.quant-aq.com/device-api/{version}/{endpoint} <<< this is the default API structure which requires a version and endpoint. Version will always be v1 (until otherwise noted), and the endpoint will vary. 

    Author: Jerry Goss
    Project: Air Partners

    I don't like brute forcing things but I should add this file to this repo and use Hwei-Shin's configuration to access the quant-aq database.

    https://github.com/airpartners/data-analysis/blob/master/quantaq_pipeline.py 
    https://github.com/airpartners/data-analysis/blob/master/pull_demo.py 
'''

import requests 
import urllib3 
import httplib2 
import httpx

with open("key-private-jerry.txt") as keyfile:
    key = keyfile.read()
    print(key)

# http -a key: GET http://api.quant-aq.com/device-api/v1/account