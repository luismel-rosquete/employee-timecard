print("Welcome to the Manager Timecard Management Portal")
from employee import Employee, p1,employeeData # This will be used to import data from the employe file.
from datetime import date
managerEmployeeID = input("What's the employee ID?")
p1.employeeID = managerEmployeeID # If the employee ID enter by the manager matches the employee ID from the data, then print it.
x = employeeData[p1.employeeID]
today = date.today()
print("**********DAY SUMMARY - " + str(today) + "*********")
print(x)
print("***************************************************")