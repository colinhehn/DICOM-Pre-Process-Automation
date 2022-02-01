import os

# Script for compiling all SARP1_2 DICOM files into a .csv file for using the "Add From File" functionality on PASS.
# It will save a load of time compared to manually adding each DICOM file in the directory in order to obtain it's info through PASS.

root_directory = 'Z:\Developers\SARP1_2'
    
os.chdir(root_directory)
dicom_list = os.listdir()

f = open('compile_for_addfromfile.txt', 'w')
f.write('File Name\n')

add_count = 0
for directory in dicom_list:
    os.chdir(directory)
    
    file_name = os.listdir()[0]
    f.write(os.path.abspath(file_name) + '\n')
    
    add_count += 1
    print('File {} added ({}).'.format(add_count, file_name))
    os.chdir(root_directory)

f.close()
os.rename('compile_for_addfromfile.txt', 'dicom_compilation.csv')