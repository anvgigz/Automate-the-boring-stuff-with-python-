import shutil, os, re

datePattern = re.compile(r"""^(.*?)     # all text before the date
                          ((0|1)?\d)-     ## One or two digits for the month    
                          ((0|1|2|3)?\d-    #one or two digits for the day
                          ((19|20)\d\d))    #four digits for the year
                          (.*?)$            #all text after the date
                          """, re.VERBOSE)


datePattern = re.compile(r"""^(1)      #All text before the date
                         (2 (3) )-      #one or more digits for month
                         (4 (5) )-      #one or two digits for the day
                         (6 (7) )       #four digits for the year
                         (8)$           # all text after the dat
                         """, re.VERBOSE)

# Loop over the files in the current directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo is None:
        continue

    # Get different parts of the file name
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)

    # Form European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart



#Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)

#rename the files.
    print(f'Renaming "{amerFilename}"" to "{euroFilename}"...')
    #shutil.move(amerFilename, euroFilename) # uncomment for testing