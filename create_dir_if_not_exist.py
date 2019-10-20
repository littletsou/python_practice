# Author : Judy
# Dsecription: To check testdir whether exists in root directory or not. 
# If not exists, create it.

import os

MESSAGE = "The directory had been existed."
testdir = "testDir"

try:
    directory = os.path.expanduser("~")
    print(directory)

    if not os.path.exists(os.path.join(directory, testdir)):
        os.makedirs(os.path.join(directory, testdir))
    else:
        print(MESSAGE)

except Exception as e:
    print(e)