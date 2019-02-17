import os
import facebook
import requests

token=os.environ['personal_fb_token']
graph=facebook.GraphAPI(access_token=token, version=3.2)

statuses=graph.get_objects()