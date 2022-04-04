from random import random
import pytest
import requests
from .shared_vars.constant_vals import *
import json
import string
import random

#This function will verify a newly added repo for the authenticated user
def test_add_repo():

  # Choose a random name
  
    letters = string.ascii_lowercase
    repo_name = ''.join(random.choice(letters) for i in range(10)) 
    repo_descr = ''.join(random.choice(letters) for i in range(20)) 

    repo_details = {
       "name": repo_name,
       "description":repo_descr,
        "private": False,
        "has_issues": False,
        "has_projects": True,
        "has_wiki": True
  }  
  
    #Convert the text to JSON, as required
    payload = json.dumps(repo_details)
    response = requests.post(repos_url,headers=headers_basic_auth,data=payload)
    add_status = response.status_code
    assert add_status == int('201')