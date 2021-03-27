from datetime import date # Import the date module to obtain today's date.
clockIn = []
clockOut = []
empID = ""

today = date.today()
print("")
print("Welcome to the Employee Timecard System - FOR CURRENT EMPLOYEES ONLY")
userRole = "Employee"
clockInTime = ""
clockOutTime = ""
nextUser = False # Will be set to False by default.
finalString = ""

employeeData = {  #This is the dictionary where the data will be stored.
}

class Employee:
  def __init__(self, employeeID, userRole, whatDay, clockInTime, clockOutTime):
    self.employeeID = employeeID
    self.userRole = userRole
    self.whatDay = whatDay
    self.clockInTime = clockInTime
    self.clockOutTime = clockOutTime

if userRole == "Employee":
    empID = input("What's your Employee ID?")
    print("Hello Employee ID #" + empID)
    clockIn = input("What's the clock-in time?")
    clockOut = input("What's the clock-out time?")
    p1 = Employee(empID, userRole, str(today), clockIn, clockOut)
    finalString = "Employee ID # " + p1.employeeID + " Day: " + p1.whatDay + " Clock-In: " + p1.clockInTime + " Clock-Out: " + p1.clockOutTime # This will be saved in the dictionary
    employeeData[p1.employeeID] = finalString # The key of the data will be the employee ID number
    print("Your clock-in/out has been successfully saved. Thank you for using the ElexSystem.")
    daySummary = input("Would you like to access your day summary?")
    if daySummary == "Y":
        x = employeeData[p1.employeeID] # Read data from the dictionary
        print(x)

    else:
        print("This system is only for employees. Please access the Manager system for manager access.")

    letsContinue = input("Would you like to conduct another transaction?")
    if letsContinue == "Yes":
        nextUser = True # While there is another transaction to be done, go back to the "main" app
        while nextUser:
            import app


    else:
        print("Okay. Good Bye!") # if there is no transaction left to complete then exit the ElexSystem.
        exit() # Exit the system