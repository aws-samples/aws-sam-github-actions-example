# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import os
import sys

sys.path.append(
    os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            os.path.pardir,
            os.path.pardir,
            os.path.pardir,
            "lambdas",
            "cleaninput"
        )
    )
)

from cleaninput import lambda_handler 

def test_cleaninput():
    event = {
        'input': {
            'input': '1 20 3'
        }   
    }

    # actual function call
    actual_response = lambda_handler(
        event=event,
        context={}
    )

    # expected response
    expected_response = {
        'input': {
            'first': '1', 
            'second': '20', 
            'third': '3'
        }
    }
    
    assert(actual_response == expected_response)
