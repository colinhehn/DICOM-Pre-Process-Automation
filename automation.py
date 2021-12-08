import pydicom
import psycopg2
import os

connection = None
root_directory = 'Z:\Project\BLF\Human Scans\Dispatch Received\IMPORT'

# Grabs new PatientID from Database (H-29502, H-29503, etc.)
def retrieve_new_PatientID():
    try:
        connection = psycopg2.connect(
            host='db.i-clic.uihc.uiowa.edu',
            database='mifar06',
            user='postgres',
            password='Ii~tyv[]?')

        with connection.cursor() as curs:
            curs.execute("SELECT mf_next_sub_autoname('H')")
            new_patient_id = curs.fetchone()
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')
    return str(new_patient_id[0])

# Declaring variables to be changed in dcmodify
PatientName = ''
PatientID = ''
StudyID = ''
SeriesDescription = ''

# Changes to designated directory, 
os.chdir(root_directory)
patient_list = os.listdir()

for patient in patient_list:    
    os.chdir(patient)
        # Do this when inside the 130002 folder
    os.chdir(root_directory)