#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self. department = department
        self.salary = salary
        
    def display_employee(self):
        return f"Name: {self.name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}"
    
    def update_employee(self, department, salary):
        if department:
            self.department = department
        if salary:
            self.salary = salary
            
class Management_System:
    def __init__(self):
        self.employees = []
        
        
    def add_employee(self, name, age, department, salary):
        new_employee = Employee(name, age, department, salary)
        self.employees.append(new_employee)
        return(f"Employee {name} has been added successfully.")
    
    def view_all_employee(self):
        try:
            if not self.employees:
                print("NO Employee to display")
            else:
                for employee in self.employees:
                    print(employee.display_employee())
        except Exception as e:
            print(f"An unexpected error occurred while viewing employees: {e}")

        
                
    def search_employee(self, name):
        found = False
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                print(employee.display_employee())
                found = True
                break
        if not found:
            print(f"Employee named {name} not found.")

    def update_employee(self, name, department=None, salary=None):
        found = False
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                employee.update_employee(department, salary)
                print(f"Employee {name} updated successfully.")
                found = True
                break
        if not found:
            print(f"Employee named {name} not found.")

    def delete_employee(self, name):
        found = False
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                self.employees.remove(employee)
                print(f"Employee {name} deleted successfully.")
                found = True
                break
        if not found:
            print(f"Employee named {name} not found.")


def main():
    system = Management_System()

    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            department = input("Enter employee department: ")
            salary = float(input("Enter employee salary: "))
            system.add_employee(name, age, department, salary)
        
        elif choice == '2':
            system.view_all_employee()
            
        elif choice == '3':
            name = input("Enter employee name to search: ")
            system.search_employee(name)
        
        elif choice == '4':
            name = input("Enter employee name to update: ")
            department = input("Enter new department (leave empty to skip): ")
            salary = input("Enter new salary (leave empty to skip): ")
            salary = float(salary) if salary else None
            system.update_employee(name, department, salary)
        
        elif choice == '5':
            name = input("Enter employee name to delete: ")
            system.delete_employee(name)
        
        elif choice == '6':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice! Please choose a number between 1 and 6.")


main()

