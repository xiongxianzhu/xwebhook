from flask import jsonify


def json_success(code=0, msg='SUCCESS', **kwargs):
    kwargs['code'] = code
    kwargs['msg'] = msg
    return jsonify(kwargs)

def json_error(code=-1, msg='ERROR', **kwargs):
    kwargs['code'] = code
    kwargs['msg'] = msg
    return jsonify(kwargs)
