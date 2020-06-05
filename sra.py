import os
import numpy as np
import matplotlib.pyplot as plt 
from github import Github 

auth_token = os.environ.get('gh_token')
# github object
g = Github(auth_token)
# This connects to the corresponding repository 
repos_obj = g.get_repo('miltonjdaz/Runescape')
import ipdb; ipdb.set_trace()

"""
def get_data(repos):
    from github import Github
    # Protecting the connection information 
    auth_token = os.environ.get('gh_token')

    # github object
    g = Github(auth_token)
    # This connects to the corresponding repository 
    repos_obj = g.get_repo('miltonjdaz/{reposname}'.format(reposname=repos))
    # This REST API will get the commits of the repository 
    newobj = repos_obj.get_commits()
    # This returns the total number of commits of the repository 
    tc = newobj.totalCount
    return tc
"""