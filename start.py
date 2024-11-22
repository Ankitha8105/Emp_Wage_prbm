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

def check_attendence():
    """Description: 
            Function to print employee is present or not
        Returns:
            Employee is present or not
        """
    
    rand_val = random.randint(0,1)
    if(rand_val == 1):
        print("Employee is present")
    else:
        print("Employee is Not present")

def main():
    display()
    check_attendence()


if __name__ == "__main__":
    main()