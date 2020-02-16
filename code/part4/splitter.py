# Following code splits the CSV file

import sys

filename = 'login_credentials'
csvfilename = open(filename+'.csv', 'r').readlines()
header = csvfilename[0] #store header values
csvfilename.pop(0) #remove header from list


write_file1 = csvfilename[0:22]
write_file2 = csvfilename[22:45]
write_file3 = csvfilename[45:68]
write_file1.insert(0, header)
write_file2.insert(0, header)
write_file3.insert(0, header)
 	  
open(str(filename)+ '1' + '.csv', 'w+').writelines(write_file1)
open(str(filename)+ '2' + '.csv', 'w+').writelines(write_file2)
open(str(filename)+ '3' + '.csv', 'w+').writelines(write_file3)