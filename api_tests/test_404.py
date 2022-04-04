import pytest
import requests
from .shared_vars.constant_vals import *


#This function attempts to view a page in repro that requires authentication
#It is expected a 404 displays in this case.
def test_404():
  # Get the response
    response = requests.get(auth_url)
    assert response.status_code == int(404)
