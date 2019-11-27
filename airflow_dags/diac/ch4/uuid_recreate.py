import pandas as pd
import os
import hashlib

dirpath = os.path.realpath(__file__)
dirpath = dirpath[:-16] # hard coded removing filename: "uuid_recreate.py"
# importing both given files into pandas dataframes
clients = pd.read_csv('{0}/files/clients.csv'.format(dirpath))
possible_uuids = pd.read_csv('{0}/files/possible_uuids.txt'.format(dirpath), header=None, names=["poss_uuid"])

# First we create an md5 hash of each possible UUID given
# There will be more possibilities than answers
    # possibilities: possible_uuids["poss_hashes"] (9k+ rows)
    # answers: clients["uuid_md5"] (1k+ rows)
possible_hashes = []
for i in possible_uuids["poss_uuid"]:
    possible_hashes.append(hashlib.md5(i.encode('utf-8')).hexdigest())
possible_uuids["poss_hashes"] = possible_hashes

# We find index matches on possible hashes (9k+ rows) to given client hashes (1k+ rows)

def index_match(poss_hash):
    for i, hash_val in clients["uuid_md5"].iteritems():
        if(poss_hash == hash_val):
            # if we find a match, return the client CSV index of that match
            return int(i)

# creating a new column which stores the client dataframe's index matching hashes
client_index = []
for i, val in possible_uuids["poss_hashes"].iteritems():
    client_index.append(index_match(val))
possible_uuids["client_index"] = client_index
# drop any rows that did not have a matching key/index with clients dataframe

possible_uuids = possible_uuids.dropna()

# first we change client index col datatype to integer 
# just in case float datatypes mess with index join on line 50's pd.concat()
possible_uuids = possible_uuids.astype({"client_index": int})

# the 9k+ index is no longer relevant because we found index
# matches between our possible uuids and original customers
# So we reindex our possible_uuids dataframe based on
# the columns `client_index`.
possible_uuids = possible_uuids.set_index(["client_index"])

# We "query" both datasets needed for our join or pandas concat
final_df_0 = pd.DataFrame(clients, columns=['name', 'email', 'date'])
final_df_1 = pd.DataFrame(possible_uuids, columns=['poss_uuid'])

# ignore_index is explicitly set to false so that the concat is based on indeces previously gathered
final_df = pd.concat([final_df_0, final_df_1], axis=1, ignore_index=False) 

# index=False so our final CSV matches the original given clients.csv
final_df.to_csv('md5-to-uuid/recovered_clients.csv', header=['name', 'email', 'date', 'uuid'], index=False)

# take that Russians
