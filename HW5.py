#!/usr/bin/env python

'''
Mimi Watanabe
IT FDN 100A Su 19
Foundations of Programming: Python
Assignment 05

This program manages a "ToDo list".

'''


# ToDo.txt location
infile = "C:\\Users\\mimim\\Intro_to_python\\Assignment05\\Todo.txt"

# read in ToDo.txt here using readlines
with open(infile, 'r') as todo_file:
    lines = todo_file.readlines() # read in file here


# create empty dictionary to store data as we loop
task_dict = {}
lstTable = []
for line in lines:
    task = (line.split(","))[0] # split the line and pull out task by index
    priority = (line.split(","))[1] # split the line and pull out prority by index
    task_dict = {"task":task,"priority":priority}
    lstTable.append(task_dict)
print(lstTable)




   # add line to add new key to a dictionary here using task ask key and priority as value

while (True):
   print("""
   Menu of Options
   1) Show current data
   2) Add a new item.
   3) Remove an existing item.
   4) Save Data to File
   5) Exit Program
   """)

   strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
  # print()  # adding a new line

   # Choice 1 -Show the current items in the table
   # loop through the dictionary here and print items
   if (strChoice.strip() == '1'):
       for i in range(len(lstTable)):
           print("task:",lstTable[i]["task"],"priority:",lstTable[i]["priority"])
   # Choice 2 - Add a new item to the list/Table
   # add a new key, value pair to the dictionary
   elif (strChoice.strip() == '2'):
       strAddTask = input("Enter a new task: ")
       strAddPrio = input("Enter a new priority: ")
       dictAdd = {}
       dictAdd["task"] = strAddTask
       dictAdd["priority"] = strAddPrio
       lstTable.append(dictAdd)
       print(lstTable)
   # Choice 3 - Remove a new item to the list/Table
   # locate key and delete it using del function
   elif (strChoice == '3'):
       lstTask = [d["task"] for d in lstTable]
       remove_key = input("Enter the task name to remove: ")
       if remove_key in lstTask:
           del lstTable[lstTask.index(remove_key)]
          # for i in range(len(lstTable)):
            #   if lstTable[i]["task"] == remove_key:
           print(lstTable)
       else:
           print(remove_key,"does not exists.")


   # Choice 4 - Save tasks to the ToDo.txt file
   # open a file handle
   # loop through key, value and write to file
   elif (strChoice == '4'):
       objFH = open("C:\\Users\\mimim\\Intro_to_python\\Assignment05\\Todo.txt",'w')
       objFH.write(str(lstTable))
       objFH.close()



   # Chocie 5- end the program
   elif (strChoice == '5'):
       break  # and Exit the program


