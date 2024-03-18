
# import jwt
# from rest_framework.exceptions import AuthenticationFailed
# from users.serializers import UserSerializer
# from users.models import User

# def get_me(request):
#     auth_header = request.headers.get('Authorization')

#     if not auth_header or not auth_header.startswith('Bearer '):
#         raise AuthenticationFailed('Unauthenticated!')

#     # Extract the token part from the header
#     token = auth_header.split(' ')[1]

#     try:
#         payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#     except jwt.ExpiredSignatureError:
#         raise AuthenticationFailed('Unauthenticated!')

#     user = User.objects.filter(id=payload['id']).first()

#     if not user:
#         raise AuthenticationFailed('User not found!')

#     serializer = UserSerializer(user)
#     return serializer.data

#     user = getattr(request, 'user', None)
#     if user is None or user.is_anonymous:
#         raise AuthenticationFailed('Unauthenticated!')
#     # Assuming you have a serializer function to serialize user data
#     return serialize_user_data(user)

import jwt
from rest_framework.exceptions import AuthenticationFailed
from users.serializers import UserSerializer
from users.models import User

def get_me(request):
    user = getattr(request, 'user', None)

    if user is None or user.is_anonymous:
        raise AuthenticationFailed('Unauthenticated!')

    serializer = UserSerializer(user)
    return serializer.data
