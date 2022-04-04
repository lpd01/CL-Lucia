import pytest
import requests
from .shared_vars.constant_vals import *


#This function verifies the content type of the api
def test_content_type():
  # Get the response
    response = requests.get(home_url, headers=headers)
    #Get the content-type from the response
    content_type = response.headers.get('content-type')
    #Verify that that the content typ is JSON
    assert content_type == expected_content_type
