from validate import *


class Employee:
  departmentdict = {}
  aadharlist = []
  panlist = []
  eid = 100

  def __init__(self, empid, fname, lname, pno, salary, age, gender, address,
               city, dob, doj, dname, designation, pan, aadhar, manager,
               emptype):
    self.empid = empid
    self.fname = fname
    self.lname = lname
    self.pno = pno
    self.salary = salary
    self.age = age
    self.gender = gender
    self.address = address
    self.city = city
    self.dob = dob
    self.doj = doj
    self.dname = dname
    self.designation = designation
    self.pan = pan
    self.aadhar = aadhar
    self.manager = manager
    self.emptype = emptype
    self.aadharlist.append(self.aadhar)
    self.panlist.append(self.pan)
    if self.dname in self.departmentdict.keys():
        self.departmentdict[self.dname].append(self.fname + " " + self.lname)
    else:
      self.departmentdict[self.dname] = [self.fname + " " + self.lname]

  def display(self):
    print("Employee ID: ", self.empid)
    print("Name: ", self.fname, self.lname)
    print("Phone Number: ", self.pno)
    print("Salary: ", self.salary)
    print("Age: ", self.age)
    print("Gender: ", self.gender)
    print("Address: ", self.address)
    print("City: ", self.city)
    print("Date of Birth: ", self.dob)
    print("Date of Joining: ", self.doj)
    print("Department Name: ", self.dname)
    print("Designation: ", self.designation)
    print("PAN Number: ", self.pan)
    print("Aadhar Number: ", self.aadhar)
    print("Manager: ", self.manager)
    print("Employee Type: ", self.emptype)
    print('-----------------------------------')

  @classmethod
  def showdep(self, dep):
    print(dep, self.departmentdict[dep])


Employees = {}
Employees[100] = Employee(100, "Kunwer", "Naveesh", "9592068383", "6000", "22", "Male", "F501 ", "Pune", "11/04/2001", "21/09/2023", "IT", "Software Engineer", "BZQPN6016P", "123456789090", "Ajay", "Full-Time")
Employees[99] = Employee(99, "Kunwer", "N", "9592068383", "3000", "22", "Male", "F501", "Pune", "11/04/2001", "21/09/2023", "Sales", "Software Engineer", "BZQPN6016P", "123456789090", "Ajay", "Full-Time")
while True:
  print("1. Add Employee Record")
  print("2. Delete The Record of Employee")
  print("3. Update Employee Details")
  print("4. Search Details of Employee")
  print("5. Display Details of All Employees")
  print("6. Display details of Employee with highest Salary")
  print("7. Display the details of Employee with lowerst salary")
  print("8. Display the Total Salary of Each Department")
  print("9. Exit")
  print('-----------------------------------------------')
  ch = int(input("Enter your choice: "))
  if ch == 1:
    empid = Employee.eid + 1
    Employee.eid += 1
    while True:
      fname = input("Enter First Name: ")
      if checkName(fname):
        break
      else:
        print("Invalid Name! Please Enter a Correct Name")
    while True:
      lname = input("Enter Last Name: ")
      if checkName(lname):
        break
      else:
        print("Invalid Name! Please Enter a Correct Name")
    while True:
      pno = input('Enter Employee Phone number: ')
      if checkMobile(pno):
        break
      else:
        print("Invalid Phone Number! Please Enter a Correct Phone Number")
    while True:
      salary = input("Enter Employee Salary: ")
      if checkSal(salary):
        break
      else:
        print('Invalid Salary! Please Enter a Correct Salary')
    while True:
      age = input("Enter Employee Age: ")
      if checkAge(age):
        break
      else:
        print("Invalid Age! Please Enter a Correct Age")
    while True:
      gender = input("Enter Employee Gender(Male/Female): ")
      gender = gender.title()
      if checkGender(gender):
        break
      else:
        print("Invalid Gender! Please Enter a Correct Gender")
    address = input("Enter Employee Address: ")
    while True:
      city = input("Enter Employee City: ")
      city = city.title()
      if checkCity(city):
        break
      else:
        print("Invalid City! Please Enter a Correct City")
    while True:
      dob = input("Enter Employee Date of Birth (dd/mm/yyyy): ")
      if checkDOB(dob):
        break
      else:
        print("Invalid Date of Birth! Please Enter a Correct Date of Birth")
    while True:
      doj = input("Enter Employee Date of Joining (dd/mm/yyyy): ")
      if checkDOB(doj):
        break
      else:
        print(
            "Invalid Date of Joining! Please Enter a Correct Date of Joining")
    while True:
      dname = input("Enter Employee Department Name: ")
      #dname = dname.title()
      if checkDep(dname):
        break
      else:
        print(
            "Invalid Department Name! Please Enter a Correct Department Name")
    while True:
      designation = input("Enter Employee Designation: ")
      #designation = designation.title()
      if checkDesignation(designation):
        break
      else:
        print("Invalid Designation! Please Enter a Correct Designation")
    while True:
      pan = input("Enter Employee PAN Number: ")
      if pan in Employee.panlist:
        print("Pan already present!")
        continue
      if checkPan(pan):
        break
      else:
        print("Invalid PAN Number! Please Enter a Correct PAN Number")
    while True:
      aadhar = input("Enter Employee Aadhar Number: ")
      if aadhar in Employee.aadharlist:
        print("Aadhar already present!")
        continue
      if checkAadhar(aadhar):
        break
      else:
        print("Invalid Aadhar Number! Please Enter a Correct Aadhar Number")
    manager = input("Enter Manager's name: ")
    manager = manager.title()
    while True:
      print('Enter Type of employee Full-Time, Part-Time or Internship: ',
            end='')
      emptype = input()
      if checkType(emptype):
        break
      else:
        print('Invalid Type! Please Enter a Correct Type')

    Employees[empid] = Employee(empid, fname, lname, pno, salary, age, gender, address, city, dob, doj, dname, designation, pan, aadhar, manager, emptype)

    print("Employee Details Entered Successfully!")
    print('---------------------------------------')
    print(f"\033[1mThe Employee ID is {empid}\033[0m")
    print('---------------------------------------')

  elif ch == 2:
    rmid = int(input("Enter Employee ID to Remove: "))
    if rmid in Employees.keys():
      Employee.departmentdict[Employees[rmid].dname].remove(Employees[rmid].fname+" "+Employees[rmid].lname)
      del Employees[rmid]
      print("Employee Removed Successfully!")
      print('----------------------------------')
    else:
      print("Employee ID not found!")
  elif ch == 3:
    while True:
      print("a. Update Name of Employee")
      print("b. Update Address of Employee")
      print("c. Update DOB of Employee")
      print("d. Update Salary of Employee")
      print("e. Exit")
      print('----------------------------')
      choice = input("Enter Choice: ")
      if choice == 'a':
        empid = int(input("Enter Employee ID: "))
        if empid in Employees.keys():
          fname = input("Enter Employee First Name: ")
          lname = input("Enter Employee Last Name: ")
          Employees[empid].fname = fname
          Employees[empid].lname = lname
          print("Name Updated Successfully!")
          print("--------------------------------")
          break
        else:
          print('Invalid Employee ID!')
      elif choice == 'b':
        empid = int(input("Enter Employee ID: "))
        if empid in Employees.keys():
          address = input("Enter Employee Address: ")
          Employees[empid].address = address
          print("Address Updated Successfully!")
          print('----------------------------')
          break
        else:
          print('Invalid Employee ID!')
      elif choice == 'c':
        empid = int(input("Enter Employee ID: "))
        if empid in Employees.keys():
          dob = input("Enter Employee Date of Birth: ")
          Employees[empid].dob = dob
          print("Date of Birth Updated Successfully!")
          print('-----------------------------')
          break
        else:
          print('Invalid Employee ID!')
      elif choice == 'd':
        while True:
          print('I. Update salary of Specific Employee')
          print(
              'II. Update salary of Employees Working in specific department')
          print("III. Update salary of all Employees")
          print("IV. Exit")
          print('-----------------------------------')           
          subchoice = input("Enter choice: ")
          if subchoice == 'I':
            empid = int(input("Enter Employee ID: "))
            if empid in Employees.keys():
              salary = int(input("Enter Employee Salary: "))
              Employees[empid].salary = int(Employees[empid].salary) + salary
              print('-------------------------')
              print("Salary Updated Successfully!")
              print('-------------------------')
              break
            else:
              print('Invalid Employee ID!')
          elif subchoice == 'II':
            dname = input("Enter Department Name: ")
            if checkDep(dname) == False:
              print('-------------------------')
              print("Invalid Department Name")
              print('-------------------------')
              continue
            salary = int(input("Enter Employee Salary: "))
            for i in Employees.keys():
              if Employees[i].dname == dname:
                Employees[i].salary = int(Employees[i].salary) + salary
                print('-------------------------')
                print("Salary Updated Successfully!")
                print('-------------------------')
                break
          elif subchoice == 'III':
            salary = int(input("Enter Employee Salary: "))
            for i in Employees.keys():
              Employees[empid].salary = int(Employees[empid].salary) + salary
              print('-------------------------')
              print("Salary Updated Successfully!")
              print('-------------------------')
              break
          elif subchoice == 'IV':
            break
          else:
            print("Invalid Choice! Please Enter a Correct Choice")
      elif choice == 'e':
        break
      else:
        print("Invalid Choice! Please Enter a Correct choice")

  elif ch == 4:
    while True:
      print("a. Search by Employee ID")
      print("b. Search by Employee Name")
      print("c. Search by Department Name")
      print("d. Exit")
      print('-------------------------')
      cho = input("Enter choice: ")
      if cho == 'a':
        empid = int(input("Enter Employee ID: "))
        if empid in Employees.keys():
          Employees[empid].display()
        else:
          print("Employee ID not found!")
      elif cho == 'b':
        fname = input("Enter Employee First Name: ")
        lname = input("Enter Employee Last Name: ")
        for i in Employees.keys():
          if Employees[i].fname == fname and Employees[i].lname == lname:
            Employees[i].display()
      elif cho == 'c':
        while True:
          depa = input("Enter Department name: ")
          if checkDep(depa):
            Employee.showdep(depa)
            break
          else:
            print("Enter a valid Department Name!")
      elif cho == 'd':
        break
      else:
        print("Invalid choice! Please Enter a correct choice")
  elif ch == 5:
    for i in Employees.keys():
      Employees[i].display()
  elif ch == 6:
    max = 0
    for i in Employees.keys():
      if int(Employees[i].salary) > max:
        max = int(Employees[i].salary)
    print('Employee with Maximum salary is/are: ')
    for i in Employees.keys():
      if int(Employees[i].salary) == max:
        print(Employees[i].fname, Employees[i].lname)
    print('-------------------------------------')
  elif ch == 7:
    min = float('inf')
    for i in Employees.keys():
      if int(Employees[i].salary) < min:
        min = int(Employees[i].salary)
    print('Employee with Minimum salary is/are: ')
    for i in Employees.keys():
      if int(Employees[i].salary) == min:
        print(Employees[i].fname, Employees[i].lname)
    print('-------------------------------------')
  elif ch == 8:
    for i in Employee.departmentdict.keys():
      total = 0
      for j in Employees.values():
        if j.dname == i:
          total += int(j.salary)
      print(i,total)
  elif ch == 9:
    break
  else:
    print("Invalid choice! Please Enter a correct choice")
