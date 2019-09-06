
from flask import Flask, render_template, request, redirect, session, jsonify
from app.branch import Branch
from app.employee import Employee

app = Flask(__name__)
app.secret_key = "The session needs this!"

@app.route('/api/branches', methods=['GET'])
def branches():        
    branch_list = Employee()
    branches = branch_list.get_branch_list()
    msg = []
    
    for branch in branches:
        branch_dets = {}
        branch_dets["city"] = branch.city
        branch_dets["name"] = branch.name
        msg.append(branch_dets)
    
    response = jsonify({'branches':msg})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/employees', methods=['GET'])
def employees():        
    employee_list = Employee()
    employees = employee_list.get_employee_list()
    msg = []
    
    for employee in employees:
        employee_dets = {}
        employee_dets["first_name"] = employee.first_name
        employee_dets["last_name"] = employee.last_name
        msg.append(employee_dets)
    
    response = jsonify({'employees':msg})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/branch_employees', methods=['POST'])
def branch_employees():
    if not request.json or 'city' not in request.json or 'name' not in request.json:
        return jsonify({"error": "bad request"}), 400
    
    branch_employee_list = Employee()
    b_employees = branch_employee_list.get_b_employee_list(request.json['city'], request.json['name'])
    msg = []
    
    for employee in b_employees:
        employee_dets = {}
        employee_dets["first_name"] = employee.first_name
        employee_dets["last_name"] = employee.last_name
        msg.append(employee_dets)
    
    response = jsonify({'branch_employees':msg})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def run():
    app.run(debug=True)
