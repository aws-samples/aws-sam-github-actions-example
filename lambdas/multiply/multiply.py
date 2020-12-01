
# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json

def lambda_handler(event, context):
   print(event)
   first = event['input']['input']['first']
   second = event['input']['input']['second']
   third = event['input']['input']['third']

   print(f"FIRST: {first}, SECOND: {second}, THIRD: {third}")
   
   result = int(first) * int(second) * int(third)
   
   print(f"RESULT: {result}")
   
   response = {
       "first": first,
       "second": second,
       "third": third,
       "result": int(result)
   }
   
   event['input'] = response

   print(event['input'])
   
   return event['input']
