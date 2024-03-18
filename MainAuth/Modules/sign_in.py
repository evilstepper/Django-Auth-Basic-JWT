from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from users.models import User
from rest_framework import status

def signin_user(email, password):
    user = User.objects.filter(email=email).first()

    #can make another funcntion in differnet class file to optimize code as component
    if user is None:
        raise AuthenticationFailed('User not found!')

    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect password!')

    serializer_class = UserSerializer

    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'status':status.HTTP_201_CREATED,
        'user': serializer_class(user).data,
        'jwt': token
    }
    
    return response
# from django.contrib.auth import authenticate
# from rest_framework.response import Response
# from users.serializers import UserSerializer
# from rest_framework.exceptions import AuthenticationFailed
# import jwt
# import datetime
# from users.models import User
# from rest_framework import status

# def signin_user(email,password):
    
#     user = authenticate(email=email, password=password)  # Using Django's authenticate method

#     if user is None:
#         raise AuthenticationFailed('User not found or incorrect password!')

#     payload = {
#         'id': user.id,
#         'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#         'iat': datetime.datetime.utcnow()
#     }

#     token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8') if hasattr(jwt.encode(payload, 'secret', algorithm='HS256'), 'decode') else jwt.encode(payload, 'secret', algorithm='HS256')

#     response = Response()
#     response.set_cookie(key='jwt', value=token, httponly=True)
#     response.data = {
#         'status': status.HTTP_200_OK,
#         'jwt': token,
#         'user': UserSerializer(user).data
#     }, 
    
#     return response

