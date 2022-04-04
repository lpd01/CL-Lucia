import pytest
import requests
import json
import jsonpath  
from .shared_vars.constant_vals import *

#This function verifies the github api version
def test_version():
  # Get the response
    response = requests.get(home_url, headers=headers)
    media_type = response.headers.get(expected_media_type)
    #media_type = str(response.headers.get(expected_media_type))
    #If the v3 text is found, the index is 0 or greater
    assert media_type.find(expected_version) > -1
