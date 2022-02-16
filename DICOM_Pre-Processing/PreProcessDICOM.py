from pydicom import dcmread
import psycopg2
import os

connection = None
root_directory = 'Z:\Project\BLF\Human Scans\Dispatch Received\IMPORT'

# Grabs new PatientID from Database (H-29502, H-29503, etc.)
def retrieve_new_PatientID():
    try:
        connection = psycopg2.connect(
            host='CONFIDENTIAL',
            database='CONFIDENTIAL',
            user='CONFIDENTIAL',
            password='CONFIDENTIAL')

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
    
    # Do this when inside the each patient folder
    PatientID = retrieve_new_PatientID()
    PatientName = patient
    StudyID = f'BLF-{patient}-BL'

    # Tunnel through single directory in between Patient folder and INSPIRATION, EXPIRATION folders
    return_directory = os.path.abspath(os.listdir()[0])
    os.chdir(os.listdir()[0])
    
    for type in os.listdir():
        
        # Acquire breath type from folder name
        if('TLC' in type):
            SeriesDescription += 'INSPIRATION '
        elif('RV' in type or 'FRC' in type):
            SeriesDescription += 'EXPIRATION '
        else:
            SeriesDescription += 'UNKNOWN '
        
        # Acquire kernel, slice thickness from DICOM file (assume all in same directory have same properties)
        os.chdir(type)
        ds = dcmread(os.listdir()[0], force=True)
        
        kernel = ds['ConvolutionKernel'].value
        slice_thickness = ds['SliceThickness'].value
        
        SeriesDescription += f'{slice_thickness} {kernel}'
        
        # dcmodify the variables of the DICOM files
        for file in os.listdir():
            ds = dcmread(file, force=True)
            ds['SeriesDescription'].value = SeriesDescription
            ds['PatientID'].value = PatientID
            ds['PatientName'].value = PatientName
            ds['StudyID'].value = StudyID
            
        # Printing to test all values have been acquired and designated correctly
        print(PatientID)
        print(PatientName)
        print(StudyID)
        print(SeriesDescription)
        print('')
            
        # Reset for new breath type folder
        SeriesDescription = ''
        os.chdir(return_directory)
        
    os.chdir(root_directory)

print('Voilà!')

# Took 1 minute 24 seconds to execute, 28 seconds per patient. That's really slow... How can we speed it up?
