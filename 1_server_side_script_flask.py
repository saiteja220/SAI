changes done

from flask import Flask, jsonify, request
import time

app = Flask(' CUSTOMER ')

cust_det = {'CUST-1':'KUMAR', 'CUST-2':'BALU'}

@app.route('/get', methods=['GET'])
def get_cust_details():
    """
    To get all customer details
    """
    time.sleep(2)
    return jsonify(cust_det)

@app.route('/create', methods=['POST'])
def create_customer():
    '''
    To create new record
    '''
    d = request.json
    cust_det.update(d)
    return jsonify(cust_det)

@app.route('/update', methods=['PUT'])
def update_emp():
    '''
    To update emp details
    '''
    d = request.json
    cust_det.update(d)
    keys = list(d.keys())
    k = keys[0]
    return ' {0} RECORD UPDATED SUCCESSFULLY'.format(k)

@app.route('/delete', methods=['DELETE'])
def delete_emp():
    '''
    To delete emp record
    '''
    d = request.json
    keys = list(d.keys())
    k = keys[0]
    del cust_det[k]
    return ' {0} RECORD DELETED SUCCESSFULLY'.format(k)


# To run app
app.run(debug=True)
 
