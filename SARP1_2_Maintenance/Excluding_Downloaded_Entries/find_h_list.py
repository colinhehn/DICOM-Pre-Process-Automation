import os

# Script for downloading only the H-Number entries we needed, as some in our Postgres Query were
# already downloaded to SARP1_2

root_directory = 'Z:\Developers\SARP1_2'
master_list_name = 'master_h_list.txt'
download_list_name = 'h_to_download.txt'

os.chdir(root_directory)
h_list = os.listdir()

del_list = []

for h in h_list:
    if h.endswith('.zip'):
        num = h.split('_')[0]
        if num not in del_list:
            del_list.append(num)

# print(del_list) SUCCESS!
# print(len(del_list)) SUCCESS! --> 54


with open(master_list_name, 'r') as file:
    lines = file.readlines()


for line in lines:
    if line.strip() not in del_list:
        with open(download_list_name, 'w') as file:
            file.write(line.strip())