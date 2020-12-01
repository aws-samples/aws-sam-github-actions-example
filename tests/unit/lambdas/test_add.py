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
            "add"
        )
    )
)

from add import lambda_handler 

def test_add():
    event = {
        "input": {
          "first": "1",
          "second": "20",
          "third": "3",
          "result": 59
        }
    }

    # actual function call
    actual_response = lambda_handler(
        event=event,
        context={}
    )

    # expected response
    expected_response = {
        'first': '1', 
        'second': '20', 
        'third': '3', 
        'result': 79
    }
    
    assert(actual_response == expected_response)
