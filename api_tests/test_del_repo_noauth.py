import pytest
import requests
from shared_vars.constant_vals import *
import json

def test_del_repo_noauth():

#Set a header that does not authenticate
   
    repo_to_delete = "Test-1"
    repo_url = owner_url + "/" + repo_to_delete
    response = requests.delete(repo_url,headers=headers)
    del_status = response.status_code 
    
    return del_status
