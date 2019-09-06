
import sqlite3
import random
import string
from app.orm import ORM
from app.branch import Branch

class Employee(ORM):

    tablename = "employee"
    fields = ["pk", "branch_pk", "first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.branch_pk = kwargs.get('branch_pk')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    def get_branch_list(self):
        return Branch.all()
        
    def get_employee_list(self):
        return Employee.all()

    def get_b_employee_list(self, city, name):
        return Employee.select_many_from_many_where(
            "employee, branch"," WHERE branch.city = ? \
            AND branch.NAME = ? AND branch.pk = \
            employee.branch_pk ORDER BY employee.last_name", (city, name))
