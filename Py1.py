import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import numpy as np

class employees:

    num_of_emp = 0
    
    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = name + "." + surname + " @company.com"

        employees.num_of_emp += 1 # prints num of emp.

    def greetings(self):

        x = print(
            "Hello {} {} we are happy to have you here".format(self.name, self.surname)
        )
        return x


emp_1 = employees("John", "Jones", "50000")

print(emp_1.greetings())
print(emp_1.name, emp_1.surname, emp_1.pay)
print(employees.num_of_emp)
