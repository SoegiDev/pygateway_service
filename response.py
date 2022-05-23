from flask import Flask,json,jsonify,request,abort

error_field = "error"
data_field = "data"
message_field = "message"
error = "Error"
message = "Message"
data = "Data"

def itsOk(resp):
    """_summary_

    Args:
        resp (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if 'error' in resp:
        error = resp['error']
    else:
        error = "Error"
    if 'message' in resp:
        message = resp['message']
    else:
        message = "Message"
    if 'data' in resp:
        data = resp['data']
    else:
        data = None
    return jsonify({
        error_field: error,
        message_field:message,
        data_field:data
        }), 200
    
def unAuthorized(resp):
    """_summary_

    Args:
        resp (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if 'error' in resp:
        error = resp['error']
    else:
        error = "Error"
    if 'message' in resp:
        message = resp['message']
    else:
        message = "Message"
    if 'data' in resp:
        data = resp['data']
    else:
        data = "Data"
    return jsonify({
        error_field: error,
        message_field:message,
        }), 401

def badRequest(resp):
    """_summary_

    Args:
        resp (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if 'error' in resp:
        error = resp['error']
    else:
        error = "Error"
    if 'message' in resp:
        message = resp['message']
    else:
        message = "Message"
    if 'data' in resp:
        data = resp['data']
    else:
        data = "Data"
    return jsonify({
        error_field: error,
        message_field:message,
        }), 400
    
def forbidden(resp):
    """_summary_

    Args:
        resp (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if 'error' in resp:
        error = resp['error']
    else:
        error = "Error"
    if 'message' in resp:
        message = resp['message']
    else:
        message = "Message"
    if 'data' in resp:
        data = resp['data']
    else:
        data = "Data"
    return jsonify({
        error_field: error,
        message_field:message,
        }), 403
    
def notFound(resp):
    """_summary_

    Args:
        resp (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if 'error' in resp:
        error = resp['error']
    else:
        error = "Error"
    if 'message' in resp:
        message = resp['message']
    else:
        message = "Message"
    if 'data' in resp:
        data = resp['data']
    else:
        data = "Data"
    return jsonify({
        error_field: error,
        message_field:message,
        }), 404
    
def unProcess(resp):
    """_summary_

    Args:
        resp (_type_): _description_

    Returns:
        _type_: _description_
    """    
    if 'error' in resp:
        error = resp['error']
    else:
        error = "Error"
    if 'message' in resp:
        message = resp['message']
    else:
        message = "Message"
    if 'data' in resp:
        data = resp['data']
    else:
        data = "Data"
    return jsonify({
        error_field: error,
        message_field:message,
        }), 422
