import os
import numpy as np
import matplotlib.pyplot as plt 
from github import Github 

auth_token = os.environ.get('gh_token')
# github object
g = Github(auth_token)
# This connects to the corresponding repository 
repos_obj = g.get_repo('miltonjdaz/Runescape')
clone = repos_obj.clone_url
print(clone)

des = repos_obj.description
print(des)

contributor = repos_obj.get_contributors
print(contributor)

gsc = repos_obj.get_stats_contributors
print(gsc)

import ipdb; ipdb.set_trace()