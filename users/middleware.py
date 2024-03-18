# # auth/middleware.py
# from django.utils.deprecation import MiddlewareMixin
# from django.http import JsonResponse
# import jwt
# from rest_framework.exceptions import AuthenticationFailed

# class SimpleTokenAuthentication(MiddlewareMixin):
#     def process_request(self, request):
#         # token = request.META.get('HTTP_AUTHORIZATION', None)
#         auth_header = request.headers.get('Authorization')

#         if not auth_header or not auth_header.startswith('Bearer '):
#             raise AuthenticationFailed('Unauthenticated!')

#         # Extract the token part from the header
#         token = auth_header.split(' ')[1]
#         if token is not None:
#             try:
#                 payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
#                 # print(payload)
#                 # Set user in request based on payload data
#             except jwt.ExpiredSignatureError:
#                 return JsonResponse({'error': 'Token expired'}, status=401)
#             except jwt.InvalidTokenError:
#                 return JsonResponse({'error': 'Invalid token'}, status=401)
#         # Optionally, handle cases where there is no token
#         # If token is required, return an error response

from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
import jwt
from users.models import User
from rest_framework.exceptions import AuthenticationFailed

class SimpleTokenAuthentication(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/api/auth/me':
            auth_header = request.headers.get('Authorization')

            if not auth_header or not auth_header.startswith('Bearer '):
                return JsonResponse({'error': 'Unauthenticated!'}, status=401)

            # Extract the token part from the header
            token = auth_header.split(' ')[1]
        
            if token is not None:
                try:
                    payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                    request.user = User.objects.get(id=payload['id'])
                except jwt.ExpiredSignatureError:
                    return JsonResponse({'error': 'Token expired'}, status=401)
                except jwt.InvalidTokenError:
                    return JsonResponse({'error': 'Invalid token'}, status=401)
        

