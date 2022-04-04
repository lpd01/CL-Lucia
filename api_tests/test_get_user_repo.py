import pytest
import requests
from .shared_vars.constant_vals import *


#This function attempts to view a page in repro that requires authentication
def test_get_user_repo():
  # Get the response
  response = requests.get(user_named_repo_url)
  #Make sure it is the user expected
        
  assert response.status_code == int(200)