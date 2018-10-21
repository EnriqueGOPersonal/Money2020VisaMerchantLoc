# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 11:27:51 2018

@author: LuisEnrique
"""

import requests
from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class GetMerchants(Resource):
    def get(self):
        #Step 1 is to get posted data by the user
        url = "https://sandbox.api.visa.com/merchantlocator/v1/locator"
        payload = " \r\n{\r\n\"header\": {\r\n\"messageDateTime\": \"2018-10-21T06:43:09.903\",\r\n\"requestMessageId\": \"Request_001\",\r\n\"startIndex\": \"0\"\r\n},\r\n\"searchAttrList\": {\r\n\"merchantName\": \"Starbucks\",\r\n\"merchantCountryCode\": \"840\",\r\n\"latitude\": \"37.363922\",\r\n\"longitude\": \"-121.929163\",\r\n\"distance\": \"2\",\r\n\"distanceUnit\": \"M\"\r\n},\r\n\"responseAttrList\": [\r\n\"GNLOCATOR\"\r\n],\r\n\"searchOptions\": {\r\n\"maxRecords\": \"5\",\r\n\"matchIndicators\": \"true\",\r\n\"matchScore\": \"true\"\r\n}\r\n}"
        headers = {
                    'Accept': "application/json",
                    'Content-Type': "application/json"
                }
            
        response = requests.post(url
                                 ,cert = (r'cert.pem'
                                          ,r'key_652b3a89-abc4-4e93-b9be-1ba15f7b35db.pem')
                                 , auth =  ("7T4IRQ7OE5A80SY55PBG21I7z99JW_vkj01xYLBVHW4XR0RaQ",
                                            "5G0k5AFEDnOLAwDC4E8nGFw")
                                 , data=payload
                                 , headers=headers)
        
        return jsonify(response.text)

api.add_resource(GetMerchants, '/')

if __name__=="__main__":
    app.run(host='0.0.0.0', port = 5000)
