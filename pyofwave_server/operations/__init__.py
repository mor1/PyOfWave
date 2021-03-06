"""
Please place files here to add operations for use with client protocols.
The name of the file will be used as the namespace and any contained public functions will be used as
operations. The information is passed as kwargs to the function.
Requests which don't match your function defination will return an error.
"""
import auth, blip, document, events, robot, wavelet
import tests

def OperationError(code, **status):
    exc = Exception()
    exc.code = code
    exc.status = status
    
    return exc