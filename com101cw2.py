employee = open ('emps.txt', 'r')
emp = employee.readlines()
#print(emp)
import time 
#This includes the time module into the program
import matplotlib.pyplot as plt
#We are importing the matplotlib module into the program


def readin():
    empFile = open('emps.txt', 'r') #Reads in employee detail file names emps.txt

    for line in empFile:
        if '#' not in line: #Ignores any line in the .txt file that included the '#' character
            print (line) #Prints each line that doesn't include the '#' character
            
    empFile.close() #Closes the txt file
    time.sleep(5)
    #Makes the program wait 5 seconds before returning the user back to the menu as to not
    #overwhelm the user with each line in the text file and the menu being presented at the same time
    menu()  

def amount():
    empFile = open('emps.txt', 'r')
    num_lines = 0 #Creates a variable to be able to count the number of records in the text file

    for line in empFile: #A for loop to count how many lines are in the text file...
        if '#' not in line: #Outside of the line(s) starting with the # symbol...

            num_lines += 1 #And adds one to the num_lines variable for such existing lines in the text file
    print ("The number of employee records in the Employee Management Tool are", num_lines)
    empFile.close()
    time.sleep(3.5) #Waits 3.5 seconds before returning the user to the menu
    menu()

def totalSalary():
    mysum = 0 #A variable to count the total of salaries recorded in the text file
    with open('emps.txt', 'r') as f: #opens the employee detail file as a variable named 'f'
        for line in f: 
            if '#' not in line: #Ignores any line in the .txt file that included the '#' character
                mysum +=int(float(line.split(",")[4]))
                #This line selects the 5th value in each record (Salary)

    finalNum = mysum
    finalNum = (round(finalNum, 2)) #Rounds the finalNum variable to 2 decimal places
    finalNum = "{:,}".format(finalNum)
    #Formats the number to add commas between each 3 digits before the decimal point
    print ("The toal salary bill acrosss all employees is", '£' +  str(finalNum))
    time.sleep(3.5)
    menu() #Returns the user to the menu 

def avgSalary():
    numLines = 0 #A variable to count all records (outside of the header) in the text file
    mysum = 0 #A variable to count the average of all salaries recorded in the text file
    
    with open('emps.txt', 'r') as f:
        for line in f:
            if '#' not in line: #Ignores the header and any line featuring the hashtag
                mysum +=int(float(line.split(",")[4])) #Selects the salary attribute in each line
                                                       #and adds each salary to the mysum variable
                numLines += 1  #Adds 1 to the numLines variable for each record in the emps.txt file
                
    finalnum = mysum / numLines
    finalnum = (round(finalnum, 2))
    #Rounds the result of the division of mysum by numLines to 2 decimal places
    finalnum = "{:,}".format(finalnum) #Formats the final number to have commas per every 3 digits
    print ("The average salary per every employee is", '£' + str(finalnum))
    time.sleep(2)
    menu()

def depts():
    dev = 0     #Declaring all variables
    devOps = 0  #for every department
    analyst = 0 #in the emps.txt file
    tester = 0  #(based off existing data)

    empFile = open('emps.txt', 'r')
    for line in empFile:        #This foor loop
        if 'Developer' in line: #checks for the attributes 'Developer', 
            dev += 1            #'DevOps' 'Analyst' and 'tester
        elif 'DevOps' in line:  #And if found, we add a value to the
            devOps += 1         #previously created variables
        elif 'Analyst' in line: #in order for us to get a count of 
            analyst += 1        #the departments in our data set
        elif 'Tester' in line:  #found in the emps.txt file
            tester += 1
    
    #The following print statements present the amount of employees in each department
    print("There are", dev, "developers in the Data set")
    print ("There are", devOps, "staff in the development operations position")
    print ("There are", analyst, "analysts")
    print ("And", tester, "staff hold the position of 'testers'")

def newEmp():
    empFile = open('emps.txt', 'a+')
    #This line opens the emp.txt file to append to it

    enum = int(input("What is the employee number of the new employee "))   #Asks the user for 
    ename = str(input("What is the name of the employee to be added? "))    #Each specified attribute 
    eAge = int(input("What is the age of the new employee "))               #matching the data structure
    position = str(input("What position does the employee hold? "))         #In our emps.txt file
    salary = int(input("What salary does the employee make? "))         #Along with data types for validation 
    years = int(input("How many years has the he/she been employed by us? (If new enter 0) "))
    
    row = str(enum) +str(', ')            #Although this isn't the most common or easiest way to
    row = row + str(ename) + str(', ')    #Add a new employee record to the list/file
    row = row + str(eAge) + str(', ')     #It was the only way I could achieve this
    row = row + str(position) + str(', ') #Without having brackets around the new record and single quotes 
    row = row + str(salary) + str(', ')   #Surrounding each attribute
    row = row + str(years)

    if enum < 0:
        print("The employe number cannot be a number less than 0")
        #Provides error message for negative value
        #This makes sure that the user can't enter a negative employee number
        newEmp()
        #Returns user to the beginning of the new employee function

    elif eAge <0:
        print("The employe age cannot be a number less than 0")
        #Provides error message for negative value
        #This makes sure that the user can't enter a negative age
        newEmp()
        #Returns user to the beginning of the new employee function

    elif salary <0:
        print("A new employee salary cannot be less than 0")
        #Provides error message for negative value
        #This makes sure that the user can't enter a negative salary
        newEmp()
        #Returns user to the beginning of the new employee function

    elif years <0:
        print("An employee's minimum number of years employeed is 0, you've entered a negative number")
        #Provides error message for negative value
        #This makes sure that the user can't enter a negative year value
        newEmp()
        #Returns user to the beginning of the new employee function

    else:
        print ("The following values have been added to the employee details file and list:", (row))
        #Shows the user the values being added to the list and emps list
        #print(emp) #This line proves that the new employee has been added to the list

        empFile.write(('\n' + (row))) #This line writes the user's inputs to the file along with a
        #newline character to seperate the new record from the latest one in the emps.txt file
        empFile.close() #Closes the emp.txt file after writing to it
        time.sleep(1.5)
        menu() #Calls the menu function 
    

def threshold():
    spec = float(input("Enter the salary that existing employee records must be greater than "))
    #Prompts the user to enter a salary to search above
    validation = 0
    #A variable to check if the input (spec) is more than 0 further down the line
    
    #Opens the emps.txt file as a readable file, regarding the file as variable 'f'
    with open('emps.txt', 'r') as f:
        print("The following employees earn over £", (spec),(":"), sep='')
        time.sleep(1)
        
        for line in f: 
            splitter = line.split(',') 
            #Splits every value in the txt file
            
            if validation > 0:
                if float(splitter[4]) > spec:
                    #Searches for all salaries above the user's input
                    print(line)
                    #And then returns those records
                    
            else:
                print("Please enter a number above 0")
                #Makes sure that the user has to enter a number greater than 0

            validation = validation + 1
            #Makes sure lines only get read once 
            numofemps = int(validation)
            
        print("""\nTotal number of employees above your threshold of £""", (spec), (":"), sep = '')
        #Shows the user the number of records above their input
                  
        print(numofemps)
        #Prints the number of employees above the user's salary they chose
            
    time.sleep(1.5)
    menu()

def deptSalaries():
    dev = 0     #Declaring all variables
    devOps = 0  #for every department
    analyst = 0 #in the emps.txt file
    tester = 0  #(based off existing data)
    
    with open('emps.txt', 'r') as f: #opens the employee detail file as a variable named 'f'
        for line in f: 
            if 'Developer' in line: #Searches for lines which include 'Developer'
                dev += int(float(line.split(",")[4])) #Adds every salary to dev variable to
                #calculate the total sum of every developer salary

            elif 'DevOps' in line: #Searches for lines which include 'DevOps'
                devOps += int(float(line.split(",")[4])) #Adds every salary to devOps variable to
                #calculate the total sum of every DevOps salary

            elif 'Analyst' in line:#Searches for lines which include 'Analyst'
                analyst += int(float(line.split(",")[4]))#Adds every salary to analyst variable to
                #calculate the total sum of every Analyst salary

            elif 'Tester' in line:#Searches for lines which include 'Tester'
                tester += int(float(line.split(",")[4]))#Adds every salary to Tester variable to
                #calculate the total sum of every Tester salary
    
    
    deptSalaries = [dev, devOps, analyst, tester]
    #Creates a list with the department salaries
    depts = ['Developers - ', 'DevOps', 'Analysts', 'Testers']
    #Sets the department variables

    plt.pie(deptSalaries, labels=depts)
    #Sets the values to be shown in the pie chart along with the labels to be used
    plt.title('Total Salaries for Each Department')
    #Sets the title for the pie chart
    plt.show()
    #Returns the pie chart to the user
            
        

def menu():
    print("\n Welcome to the employee management tool, please type the digit for \n the option you would like to select; ")
    print("""\n 1. Employee summary statement \n 2. Employee detail list \n 3. Total salary bill 
 4. Average salary bill \n 5. Add a new employee \n 6. Number of employees in each position type 
 7. Find employee records above your chosen salary threshold \n 8. Quit the program 
 9. Show how salaries are distributed across each department\n""")
    #Above are the options to be presented to the user
    
    #User's input to choose which option they'd like
    choice = int(input("Option choice: "))
    
    if choice < 1 or choice > 9:    #If the user enters an option that isn't present in the menu
        print ("Sorry but", choice, "isn't a listed option") #This message will appear
        time.sleep(2)               #Letting them know that they've made a mistake
        menu()                      #And then returns them to the menu

    if choice == 8:
        exit() #Closes the program

    #The following if statements call the function matching the user's choice
    if choice == 1:
        amount()
        time.sleep(5)  

    if choice == 2:
        print("Here are all employee records: \n")
        time.sleep(1)
        readin()
        
    if choice == 3:
        totalSalary()

    if choice == 4:
        avgSalary()

    if choice == 5:
        newEmp()
        
    if choice == 6:
        depts()
        time.sleep(2)
        menu()

    if choice == 7:
        threshold()

    if choice == 9:
        deptSalaries()
        menu()
        


menu()
#This line calls the menu function created above
        

