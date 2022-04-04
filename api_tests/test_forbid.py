import pytest
import requests
from requests.auth import HTTPBasicAuth
from .shared_vars.constant_vals import *

#This function attempts to post to the repos endpoint and verifies failure
#This endpoint does not allow data to be uploaded
#Data may only be retrieved from this endpoint

def test_forbid():
 
    #Attempt to login with incorrect data
    #Continually fail to authenticate and verify that there is a 403
    x = 0
    
    while x < 50:
        response = requests.get(home_url, headers=headers,
                            auth=HTTPBasicAuth(login_uid, login_pwd))
 
        x+=1
    
    assert response.status_code == int("403")