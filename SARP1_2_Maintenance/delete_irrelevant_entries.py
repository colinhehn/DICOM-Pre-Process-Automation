import os

# Script for removing files in a directory with certain keywords/tags attached to them.
# In this case, every file containing SCOUT, DETAIL, or Topogram is deleted.

root_directory = 'Z:\Developers\SARP1_2'

os.chdir(root_directory)
h_list = os.listdir()

irrelevant_count = 0
total_count = 0

for h in h_list:
    if h.endswith('.zip'):
        total_count+= 1
        
        for value in ['scout', 'topogram', 'detail']:
            if value in h.lower():
                irrelevant_count+= 1
                os.remove(h)
                
print(len(os.listdir()))