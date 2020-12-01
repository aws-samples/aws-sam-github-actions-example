# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json

def lambda_handler(event, context):
    print(event)
    input_vals = event['input']
    
    values = input_vals['input'].split(" ")
    
    input_massaged = {
        "first": values[0],
        "second": values[1],
        "third": values[2]
    }
    
    event['input'] = input_massaged
    
    return event
