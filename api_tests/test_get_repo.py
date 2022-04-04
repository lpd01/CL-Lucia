import pytest
import requests
from .shared_vars.constant_vals import *


#This function attempts to view a page in repro that requires authentication
#It is expected a 404 displays in this case.
def test_get_repo():
  # Get the response
    response = requests.get(public_repos)
    assert response.status_code == int(200)