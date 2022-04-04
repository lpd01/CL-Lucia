import pytest
import requests
from .shared_vars.constant_vals import *


#This function attempts to post to the repos endpoint and verifies failure
#This endpoint does not allow data to be uploaded
#Data may only be retrieved from this endpoint

def test_post_repo():
  # Get the response
    #Attempt to post random text
    response = requests.post(repo_url,data_to_post)
    assert response.status_code == int("403")
 

  


