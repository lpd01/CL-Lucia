import pytest
import requests
from .shared_vars.constant_vals import *

#This function will verify if a redirect code is returned for a given URL
def test_redirect(): 
    #Attempt to access this page but do not allow redirects
    response = requests.get(repo_url_redirect, headers=headers, allow_redirects=False)
   #A 300 code is expected here. 
    str_code = str(response.status_code)                         
    assert str_code.find('3') > -1