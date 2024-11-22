'''
    @Author:Ankitha
    @Date: 22-11-2024
    @Last Modified by: Ankitha
    @Last Modified time: 22-11-2024
    @Title : Employee-Wage computation problem
'''
import random

def display():
    """
    Description:
        This functtion to display print statment
    Returns:
        None
    """
    print("Welcome to Employee Wage Computation Program !!!")

def check_attendence(num_emp):
    """Description: 
            Function to print employee is present or not
        Parameters:
            num_emp : Number of employees
        Returns:
            Employee is present or not
        """
    for emp in range(1,num_emp+1):
        rand_val = random.randint(0,1)
        if(rand_val == 1):
            print(f"Employee{emp} is present")
        else:
            print(f"Employee{emp} is Not present")

def main():
    display()
    num_emp = int(input("Enter the total number of employees :"))
    check_attendence(num_emp)

if __name__ == "__main__":
    main()