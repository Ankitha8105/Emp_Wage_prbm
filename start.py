'''
    @Author:Ankitha
    @Date: 22-11-2024
    @Last Modified by: Ankitha
    @Last Modified time: 22-11-2024
    @Title : Employee wage computation

'''
import random

class Employee:
    def __init__(self, hr_wage, total_hr_per_day=None, total_num_days_per_month=None, num_hrs=None):
        """
        Description:
            Initializes an Employee object with hourly wage and either daily/hourly data
        """
        self.hr_wage = hr_wage
        self.total_hr_per_day = total_hr_per_day
        self.total_num_days_per_month = total_num_days_per_month
        self.num_hrs = num_hrs

    @staticmethod
    def display():
        """
        Description:
            Function to display the welcome message.
    
        Returns:
            welcome message on display
        """
        print("Welcome to Employee Wage Computation Program !!!")

    @staticmethod
    def check_attendance():
        """
        Description:
            Function to check if employee is present or not.
    
        Returns:
            Employee is present or not
        """
        rand_val = random.randint(0, 1)
        if rand_val == 1:
            print("Employee is present")
        else:
            print("Employee is Not present")

    @staticmethod
    def cal_wage(hr_wage, total_hr):
        """
        Description:
            Function to calculate wage per day.
        Parameters:
            hr_wage: per hour wage
            total_hr: total hours worked in a day
        Returns:
            Total wage for the day
        """
        return total_hr * hr_wage
    
    @staticmethod
    def parttime_wage(parttime_hr, hr_wage):
        """
        Description:
            Function to calculate part-time employee wage.
        Parameters:
            parttime_hr: total hours worked part-time
            hr_wage: hourly wage
        Returns:
            Wage for part-time employee
        """
        return parttime_hr * hr_wage

    @staticmethod
    def cal_wage_per_month(num_months, wage_per_hr):
        """
        Description:
            Function to calculate total wage per month.
        Parameters:
            wage_per_hr: wage per hour
            num_months: number of months
        Returns:
            Total wage for the months
        """
        return num_months * 20 * wage_per_hr

    @staticmethod
    def calculate_wages(hourly_wage, num_days, working_hr):
        """
        Description:
            Function to calculate total wage for the month based on working hours and days.
        Parameters:
            hourly_wage: wage per hour
            num_days: number of days worked
            working_hr: hours worked per day
        Returns:
            Total wage for the month
        """
        total_wage = 0
        while num_days <= 20 and working_hr <= 100:  
            total_wage += hourly_wage * working_hr  
            num_days += 1  
            working_hr += 8  # Increase working hours by 8 each day
        
        return total_wage
    
    @classmethod
    def cal_empwage(cls,hr_wage,num_hrs):
        """
        Description:
            Function to calculate wage per day.
        Parameters:
            hr_wage: per hour wage
            total_hr: total hours worked in a day
        Returns:
            Total wage for the day
        """
        return hr_wage * num_hrs
        

Employee.display()
Employee.check_attendance()


day_wage = Employee.cal_wage(20, 8)
print(f"The total wage per day is: {day_wage}")


print(f"The part-time employee wage is: {Employee.parttime_wage(8, 20)}")


print(f"The total amount of wage per month is: {Employee.cal_wage_per_month(2, 20)}")


print(f"The total wage is: {Employee.calculate_wages(20, 1, 8)}")


Employee_obj = Employee(20, num_hrs=8)

wage = Employee.cal_empwage(20,8)
print(f"Claculating employee wage using classmethod : {wage}")
