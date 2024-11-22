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
    """
        Description: 
            Function to print employee is present or not
        Returns:
            Employee is present or not
    """
    rand_val = random.randint(0,1)
    if(rand_val == 1):
        print("Employee is present")
    else:
        print("Employee is Not present")

def cal_wage(hr_wage,total__hr):
    """
        Description: 
            Function to calculate wage per day
        parameters:
            hr_wage: per hour wage
            total_hr:total number of hours
        Returns:
            returns total amount of wage per day
    """
    wage_per_day = total__hr*hr_wage
    return wage_per_day

def parttime_wage(parttime_hr,hr_wage):
    """
        Description: 
            Function to calculate part time employee wage 
        parameters:
            hr_wage: per hour wage
            parttime_hr:total number of hours
        Returns:
            returns total amount of part time employee wage
    """
    return parttime_hr*hr_wage

def main():
    display()
    check_attendence()
    day_wage = cal_wage(20,8)
    print(f"The total wage per day is :{day_wage}")
    print(f"The part time employee wage is :{parttime_wage(8,22)}")

if __name__ == "__main__":
    main()