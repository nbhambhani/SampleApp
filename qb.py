import Customer
from utils import configRead 
from utils import request_methods
from flask import session

# Create a customer object with customer data from working dictionary
def create_customer(my_customer):
    full_name = my_customer['Full Name']
    name_list = full_name.split(' ')
    first_name = name_list[0]
    last_name = name_list[-1]
    if len(name_list) > 2:
        middle_name = str(name_list[1:len(name_list) - 1])
    else:
        middle_name = ''

    customer = Customer.Customer(first_name, last_name, middle_name, my_customer['Phone'], my_customer['Email'])
    return customer

# Add selected lead as a customer to QBO
def add_customer(customer):
    # set the request body for create_customer
    try:
        req_body = {}
        req_body["GivenName"] = customer.GivenName
        req_body["MiddleName"] = customer.MiddleName
        req_body["FamilyName"] = customer.FamilyName
        req_body["PrimaryPhone"] = {}
        (req_body["PrimaryPhone"])["FreeFormNumber"] = customer.PrimaryPhone
        req_body["PrimaryEmailAddr"] = {}
        (req_body["PrimaryEmailAddr"])["Address"] = customer.PrimaryEmailAddr
    except AttributeError:
        print 'Customer object has no attributes'
    
    try:
        realm_id = session.get('realm_id')
    except:
        realm_id = None
        print 'Realm Id not found.'

    base_url = configRead.get_api_url() + realm_id
    url = base_url + '/customer' + configRead.get_minorversion(4)
    request_data = {'payload': req_body, 'url': url}
    req_status_content = request_methods.post(request_data)
    return req_status_content
    




