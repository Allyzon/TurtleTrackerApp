#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Allison Pearce (allison.a.pearce@duke.edu)
# Date:   Fall 2020
#----------------------

#create a variable pointing to the data file
file_name = './Data/raw/sara.txt'

#create a file object from the file
file_object=open(file_name,'r')

#Read contents of file into a list
line_list=file_object.readlines()

#close the file
file_object.close()

# Iterate through all lines in the linelist 
for lineString in line_list:
    if lineString[0] in ("#", "u"): continue 


#split the string into a list of data items
lineData= lineString.split()

#extract items in list into variables 
record_id =lineData [0]
obs_date = lineData [2]
obs_lc =lineData [4]
obs_lat = lineData [6]
obs_lon= lineData [7]

#print the location of Sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon}on {obs_date}")
