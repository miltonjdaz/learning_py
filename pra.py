from github import Github 
import os
import numpy as np
import matplotlib.pyplot as plt

# Protecting the connection information  
auth_token = os.environ.get('gh_token')

g = Github(auth_token)

# Using the first repo
repos_obj = g.get_repo('miltonjdaz/Runescape')  

newobj = repos_obj.get_commits()

tc = newobj.totalCount

print(tc)

# learning_py
repos_obj2 = g.get_repo('miltonjdaz/learning_py')  

newobj2 = repos_obj2.get_commits()

tc2 = newobj2.totalCount

print(tc2)

# REST_API_project
repos_obj3 = g.get_repo('miltonjdaz/REST_API_project')  

newobj3 = repos_obj3.get_commits()

tc3 = newobj3.totalCount

print(tc3)
# import ipdb; ipdb.set_trace()

objects = ('Runescape', 'learning_py', 'REST_API_project')
y_pos = np.arange(len(objects))
performance = [tc, tc2, tc3]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of commits')
plt.title('The repositories')

plt.show()