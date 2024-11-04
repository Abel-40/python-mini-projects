# Employee Attendance System

This project implements an Employee Attendance System that allows for tracking employee check-ins and check-outs. It provides functionalities to manage employee records, check attendance status, and evaluate timeliness based on defined office hours. The main idea of this project is to demonstrate Object-Oriented Programming (OOP) principles in Python, along with practices in unit testing and the creation of test cases.

## Features

- **Employee Management**: Add and manage employee records.
- **Check-in/Check-out**: Record when employees check in and out of the workplace.
- **Timeliness Evaluation**: Determine if employees are late based on their check-in times.
- **Attendance Reporting**: List employees, their check-in times, and their attendance status.

## Classes

### Employee

The `Employee` class represents an employee in the system.

#### Attributes:
- `name` (str): The name of the employee.
- `employee_id` (str): The unique identifier for the employee.
- `__checks_in_time` (str): The time the employee checked in.
- `__checks_out_time` (str): The time the employee checked out.
- `is_present` (bool): The presence status of the employee.

#### Methods:
- `check_in()`: Records the current time as the check-in time and sets the employee as present.
- `check_out()`: Records the current time as the check-out time and updates the employee's presence status.
- `is_late()`: Checks if the employee is late compared to the defined check-in time.
- `__str__()`: Returns a string representation of the employee object.

### AttendanceSystem

The `AttendanceSystem` class manages a list of employees and their attendance.

#### Attributes:
- `employees` (list): A list of `Employee` objects.
- `office_start_time` (datetime): The official start time of the workday.

#### Methods:
- `add_employee(employee)`: Adds an employee to the attendance system.
- `list_employees()`: Prints the list of employees with their check-in times.
- `check_in_employee(employee_id)`: Checks in the employee with the given ID.
- `check_out_employee(employee_id)`: Checks out the employee with the given ID.
- `rank()`: Ranks employees based on their check-in times and identifies timely and tardy employees.
- `all_present_employee()`: Lists all employees currently present.
- `all_check_out_employee()`: Lists all employees who have checked out.

## Usage

1. **Creating Employees**:
   - Create instances of the `Employee` class for each employee you want to add.

2. **Managing Attendance**:
   - Create an instance of the `AttendanceSystem` class and use its methods to add employees, check them in and out, and generate attendance reports.

```python
employee1 = Employee('Abel Addis', 'Nsr/020/14')
attendance_system = AttendanceSystem()
attendance_system.add_employee(employee1)
attendance_system.check_in_employee('Nsr/020/14')
attendance_system.check_out_employee('Nsr/020/14')
