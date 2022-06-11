from flask import jsonify, make_response


def stringSpelter(str=None):
    if (str):
        return str.replace(';', ' ').replace(',', ' ').replace('.', ' ').replace('،', ' ').replace('-', ' ').split()
    else:
        return ''


home = '/'
homeApi = '/api/v1'


def response(messages, errors, statusCode):
    return make_response(jsonify(
        {
            'message': messages,
            'errors': errors,
        }
    ), statusCode)
