from rest_framework.response import Response

def sign_out_user(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response
