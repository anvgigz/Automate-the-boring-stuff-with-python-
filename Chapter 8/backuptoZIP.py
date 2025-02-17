import zipfile, os

def backupToZip(folder):
    # backup the entire contents ogf "folder" into a ZIP file.

    folder = os.path.abspath(folder)    #Make sure the folder is absolute

    #Figure out the filename this code should use based on 
    # What files already exist

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    #Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f" Adding files in {foldername}...")
        #Add the current folder to the zip file.
        backupZip.write(foldername)

        ##Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('zip'):
                continue # dont back upo the backup ZIP files
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Done')





backupToZip('C:\\delicius')