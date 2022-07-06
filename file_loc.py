'''
-------------------------- Brief desciption of file_loc.py --------------------------

This file basically displays all the available datasets for training our model
and allows user to select one as per his choice and then it returns the
relative path of that csv file to the caller.

in order to use it in your program simply "import file_loc as fl" at top. it imports
it from current working directory if found.

then simply call "fl.give_location()" to get the relative location of the desired file
and use it accordingly.

-------------------------- general file structure ---------------------------
ML_project
->Data folder(all csv files stored)
-> file_loc.py
-> main.py
.....
.....(to be worked upon)


---------------------------  Documentation for help   ------------------------------

🌟How to List All Files of a Directory

Getting a list of files of a directory is easy as pie! Use the listdir() and isfile() functions of an os module to list all files of a directory. Here are the steps.

🌟Import os module
This module helps us to work with operating system-dependent functionality in Python. The os module provides functions for interacting with the operating system.

--Use os.listdir() function
The os.listdir('path') function returns a list containing the names of the files and directories present in the directory given by the path.

--Iterate the result
Use for loop to Iterate the files returned by the listdir() function. Using for loop we will iterate each file returned by the listdir() function

--Use isfile() function
In each loop iteration, use the os.path.isfile('path') function to check whether the current path is a file or directory. If it is a file, then add it to a list. This function returns True if a given path is a file. Otherwise, it returns False.



🌟Difference between return and yield python
The Yield keyword in Python is similar to a return statement used for returning values in Python which returns a generator object to the one who calls the function which contains yield, instead of simply returning a value. The main difference between them is: The yield python return statement that stops the execution of the function. Whereas, the yield statement only pauses the execution of the function. Another difference is return statements are never executed. whereas, yield statements are executed when the function resumes its execution.

Advantages of yield:

Since it stores the local variable states, hence overhead of memory allocation is controlled.
Since the old state is retained, the flow doesn’t start from the beginning and hence saves time.

SOURCEs :- 
1. https://pynative.com/python-list-files-in-a-directory/
2. https://www.geeksforgeeks.org/python-check-if-a-directory-is-empty/#:~:text=To%20check%20whether%20a%20directory,directories%20in%20the%20specified%20directory.
3. https://www.geeksforgeeks.org/python-yield-keyword/#:~:text=Yield%20is%20a%20keyword%20in,keyword%20is%20termed%20a%20generator.
4.https://stackoverflow.com/questions/33323715/python-evenly-space-output-data-with-varying-string-lengths
'''

import os


def get_files(path):
    if len(os.listdir(path)) == 0:
        print("Sorry for inconveineince ! nothing to show in the entered folder")
    else:
        print("\nAll the avalable datasets are listed below :- \n")

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def give_location():
    flag = 0
    company = {}
    for file in get_files(r'.\\Data\\'):#relative path with respect to current directory
        filename = file[:-4]
        flag += 1
        company[flag] = str(file)
        print("%3d.%-15s" % (flag,filename), end = "\t")
        if flag%5 == 0:#after 5 names printed go to next line
            print()
    else:
        print("\n\nPlease enter the Company(only list number)to predict : ", end = "")
        option = input()
        while(not option.isdigit()): option = input("Please enter a valid number to proceed further : ")
        while(int(option) not in company.keys()): option = input("Please enter a valid number to proceed further : ")
        
        rel_loc = r".\\Data\\"+company[int(option)]
        #print(rel_loc)
        return rel_loc
