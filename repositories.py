import os
import requests as req
from github import Github, Auth

token = os.environ['GITHUB_API_KEY']
auth = Auth.Token(token)
github = Github(auth=auth)

github.get_user().login
orgs = github.get_organization('app-sentinel')
            
print(orgs.login)
print(orgs.description)
print(orgs._repos_url.value)
# get_all_repositories()

def get_all_repositories():
    headers = {"Authorization": f"Bearer {token}"}
    res = req.get(orgs._repos_url.value, headers=headers)
    
    print(res.json())
    
get_all_repositories()