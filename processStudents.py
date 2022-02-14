''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv
from xml.etree.ElementPath import get_parent_map
from matplotlib.cbook import open_file_cm

# create a file object to open the file in read mode
students = open('students.csv', 'r')


# create a csv object from the file object
students_file = csv.reader(students, delimiter = ',')

#skip the header row
next(students_file)

#create an outfile object for the pocessed record
outfile = open('processedStudents.csv', 'w' )


#create a new dictionary named 'student_dict'
student_dict ={}

#use a loop to iterate through each row of the file

for record in students_file: 
    student_dict["student id"] = record[0]
    student_dict["Pin"] = record[1]
    student_dict["First Name"] = record[2]
    student_dict["last Name"] = record[3]
    student_dict["city"] = record[4]
    student_dict["state"] = record[5]
    student_dict["Major"] = record[6]
    student_dict["Classifcation"] = record[7]
    student_dict["gpa"] = record[8]


print(student_dict)

    #check if the GPA is below 3.0. If so, write the record to the outfile
if student_dict['gpa']:
    outfile.write()
        

    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    




#print the entire dictionary
print(student_dict)

#Print the student id 
print(student_dict['gpa'])

#print out the corresponding GPA from the dictionary
print(student_dict["student id"]["gpa"])


#close the outfile
outfile.close()







