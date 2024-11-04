from datetime import *
class Employee:

  def __init__(self,name,employee_id):
    self.name = name
    self.employee_id = employee_id
    self.__checks_in_time = None
    self.__checks_out_time = None
    self.is_present = False

  def set_check_in_time(self,time):
    current_time = datetime.now()
    formated_current_time = current_time.strftime("%H:%M")
    self.__checks_in_time = formated_current_time

  def check_in(self):
    current_time = datetime.now()
    formated_current_time = current_time.strftime("%H:%M")
    self.__checks_in_time = formated_current_time
    self.is_present = True
  
  def check_out(self):
    if self.is_present:
      current_time = datetime.now()
      formated_current_time = current_time.strftime("%H:%M")
      self.__checks_out_time = formated_current_time
      self.is_present = False
    else:
      print("employee is not check in")

  def get_check_in_time(self):
    return self.__checks_in_time
  
  def get_check_out_time(self):
    return self.__checks_out_time
    
  def is_late(self):
    check_in_time = datetime.strptime(self.__checks_in_time, "%H:%M")
    company_check_in_time = datetime.strptime("1:00", "%H:%M")
    return check_in_time > company_check_in_time
  
  def __str__(self):
    return f"Employe Name: {self.name} Employe_id: {self.employee_id} Present: {self.is_present}"
  def __lt__(self, other):
    return self.__checks_in_time < other.__checks_in_time



class AttendanceSystem:

  def __init__(self,employees = None):
    if employees == None:
      employees = []              
    self.employees = employees
  
  office_start_time = datetime.strptime("9:00", "%H:%M")

  def add_employee(self,employee):
    self.employees.append(employee)
  
  def list_employees(self):
    for employee in self.employees:
      print(f"{employee} check_in_time: {employee.get_check_in_time()}\n")
  
  def check_in_employee(self,employee_id):
    employee = (next((emp for emp in self.employees if emp.employee_id == employee_id), None))
    if employee is None:
      print("Employee not found")
    else:
      employee.check_in()

  def check_out_employee(self,employee_id):
    employee = (next((emp for emp in self.employees if emp.employee_id == employee_id), None))

    if employee is None:
      print("Employee not found")
    else:
      employee.check_out()

  def rank (self):
    employees = sorted(self.employees)
    for emp in employees:
      if AttendanceSystem.office_start_time >= emp.get_check_in_time():
        print("Timely employees")
        print(f"{emp} check in time: {emp.get_check_in_time()}\n")
      else:
        print("Tardy employes ")
        print(f"{emp} check in time: {emp.get_check_in_time()}\n")

  def all_present_employee(self):
    present_employee = [emp for emp in self.employees if emp.is_present == True]
    for present_emp in present_employee:
      print(f"{present_emp}  check_in_time: {present_emp.get_check_in_time()}\n")

  def all_check_out_employee(self):
    check_out_employee = [emp for emp in self.employees if emp.is_present == False]
    for check_out_emp in check_out_employee:
      print(f"{check_out_emp}  check_in_time: {check_out_emp.get_check_in_time()} check_out_time: {check_out_emp.get_check_out_time()}\n")





employee1 = Employee('Abel Addis', 'Nsr/020/14')
employee2 = Employee('Betty Alemu', 'Nsr/021/14')
employee3 = Employee('John Doe', 'Nsr/022/14')
employee4 = Employee('Jane Smith', 'Nsr/023/14')
employee5 = Employee('Michael Brown', 'Nsr/024/14')
employee6 = Employee('Sarah Johnson', 'Nsr/025/14')
employee7 = Employee('Daniel Yonas', 'Nsr/026/14')
employee8 = Employee('Lily White', 'Nsr/027/14')
employee9 = Employee('Chris Green', 'Nsr/028/14')
employee10 = Employee('Emma Davis', 'Nsr/029/14')

Atech_employee_list = [employee1,employee2,employee3,employee4,employee5,employee6,employee7,employee7,employee8,employee9,employee10]



Attendace_for_Atech_company = AttendanceSystem(Atech_employee_list)

Attendace_for_Atech_company.list_employees()

Attendace_for_Atech_company.check_in_employee('Nsr/020/14')
Attendace_for_Atech_company.check_in_employee('Nsr/020/14')
Attendace_for_Atech_company.check_in_employee('Nsr/021/14')
Attendace_for_Atech_company.check_in_employee('Nsr/022/14')
Attendace_for_Atech_company.check_in_employee('Nsr/023/14')
Attendace_for_Atech_company.check_in_employee('Nsr/024/14')
Attendace_for_Atech_company.check_in_employee('Nsr/025/14')
Attendace_for_Atech_company.check_in_employee('Nsr/026/14')
Attendace_for_Atech_company.check_in_employee('Nsr/027/14')
Attendace_for_Atech_company.check_in_employee('Nsr/028/14')
Attendace_for_Atech_company.check_in_employee('Nsr/029/14')



Attendace_for_Atech_company.check_out_employee('Nsr/020/14')


Attendace_for_Atech_company.all_present_employee()

