################### URLs/URIs ################

#This is the base URL for github
home_url = 'https://api.github.com'
#This is the repos endpoint
repos_url = 'https://api.github.com/user/repos'
#This is the base URL for this github test
base_url = 'https://docs.github.com'
#This is what to add to the base url to access the repo location
repo_loc = '/en/rest/reference/repos'
#This is the URL where the repository lives
repo_url = base_url + repo_loc
repo_url_redirect = 'http://docs.github.com/en/rest/reference/repos'
#This is a URL that requires authentication
auth_url = 'https://api.github.com/user/repos'
#This is a URL that lists publi repos
public_repos = 'https://api.github.com/repositories'
#This is the owner URL for the test user
owner_url= 'https://api.github.com/repos/lpd01'



################### Constants ################

#This is the expected media type
expected_media_type = 'X-GitHub-Media-Type'
#This is the expected version
expected_version = 'github.v3'
#This is the header value to pass
headers = {'Accept': 'application/vnd.github.v3+json'}
scope_headers = {'Accept': 'application/vnd.github.v3+json',
                 'X-OAuth-Scopes': 'repo, user',
                 'X-Accepted-OAuth-Scopes': 'user'
                 }  

headers_basic_auth = {
    'Content-Type': 'application/json',
     'Authorization':'Basic bHVjaWFfcGFsZXJtb0B5YWhvby5jb206Z2hwX1lQa2NYSXZEYUFjczAxQm55OE8yQjZhWWxRUFhJaTFUbFN4VA==', 
    'Accept': 'application/vnd.github.v3+json',
    'X-OAuth-Scopes': 'repo, user',
    'X-Accepted-OAuth-Scopes': 'user'
  }

#This is the expected content-tyoe
expected_content_type = 'application/json; charset=utf-8'

################### Data ################
#Used in test to verify post is not allowed 
data_to_post= {
                  "repo name" : "repo1",
                  "repo link" : "repo1_link"
                }
login_uid = 'lucia_palermo@yahoo.com'
login_pwd = 'password'
repo_id = 'lpd01'
test_repo = 'playground'
user_token ='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@github.com'
user_token_RWD = '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'
#This is a test user repo url
user_repo_url = 'https://' + user_token + '/' + repo_id
user_named_repo_url = 'https://' + user_token + '/' + repo_id + '/' + test_repo
user_add_url = 'https://' + user_token + 'api.github.com/user/repos'
