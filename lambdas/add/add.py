# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json

def lambda_handler(event, context):
   print(event)
   first = event['input']['first']
   second = event['input']['second']
   third = event['input']['third']
   result = event['input']['result']
   
   print(f"FIRST: {first}, SECOND: {second}, THIRD: {third}")
   
   result = int(result) + int(second)
   
   print(f"RESULT: {result}")
   
   response = {
       "first": first,
       "second": second,
       "third": third,
       "result": int(result)
   }
   
   event['input'] = response
   
   return event['input']
