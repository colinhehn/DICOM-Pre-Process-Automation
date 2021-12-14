import os

# Script made to double check what unique entries existed in a text file full of H-Numbers.
# Needed to see how many UNIQUE entries there were in the query Patrick sent me.

master_list_name = 'master_h_list.txt'
download_list_name = 'h_to_download.txt'

with open(master_list_name, 'r') as file:
    lines = file.readlines()

h_list = []

for line in lines:
    if line.strip() not in h_list:
        h_list.append(line.strip())
        
print(h_list)
print(len(h_list))