from github import Github 
import os

# Protecting the connection information  
auth_token = os.environ.get('gh_token')

g = Github(auth_token)

# Using the first repo
repos_obj = g.get_repo('miltonjdaz/Runescape')  

newobj = repos_obj.get_commits()

tc = newobj.totalCount

print(tc)

import ipdb; ipdb.set_trace()