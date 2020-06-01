import os
import numpy as np
import matplotlib.pyplot as plt

# Protecting the connection information  

repos_list = ['learning_py', 'Runescape', 'REST_API_project']

def get_data(repos):
    from github import Github
    auth_token = os.environ.get('gh_token')

    # github object
    g = Github(auth_token)
    # repos object
    repos_obj = g.get_repo('miltonjdaz/{reposname}'.format(reposname=repos))
    newobj = repos_obj.get_commits()
    tc = newobj.totalCount
    # type(repos_obj)
    # description
    return tc

total_count = []
for i in repos_list:
    print(get_data(i))
    total_count.append(get_data(i))
print(total_count)

# Making the bar graph
objects = ('Runescape', 'learning_py', 'REST_API_project')
y_pos = np.arange(len(objects))
performance = [total_count[0], total_count[1], total_count[2]]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)

plt.ylabel('Number of Commits')
plt.xlabel('The Repositories')
plt.title('Total Number of Commits in Each Repository')
plt.show()

# import ipdb; ipdb.set_trace()
"""
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
"""