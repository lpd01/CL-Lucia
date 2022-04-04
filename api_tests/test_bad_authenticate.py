import pytest
import requests
from requests.auth import HTTPBasicAuth
from .shared_vars.constant_vals import *

#This function attempts to post to the repos endpoint and verifies failure
#This endpoint does not allow data to be uploaded
#Data may only be retrieved from this endpoint

def test_bad_authenticate():
    #Attempt to login with incorrect data
    response = requests.get(auth_url, headers=headers,
                            auth=HTTPBasicAuth(login_uid, login_pwd))
    
    assert response.status_code == int("401")