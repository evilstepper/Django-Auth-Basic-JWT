from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
import jwt
from users.models import User
from rest_framework.exceptions import AuthenticationFailed

class SimpleTokenAuthentication(MiddlewareMixin):
    def process_request(self, request):
        # Check if the request path is '/api/auth/me'
        if request.path == '/api/auth/me':
            auth_header = request.headers.get('Authorization')
            
            if not auth_header or not auth_header.startswith('Bearer '):
                return JsonResponse({'error': 'Unauthenticated!'}, status=401)

            # Extract the token part from the header
            token = auth_header.split(' ')[1]
            
            if token is not None:
                try:
                    # Decode the token
                    payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                    # Get the user object from the database using the user ID stored in the token payload
                    request.user = User.objects.get(id=payload['id'])
                
                except jwt.ExpiredSignatureError:
                    return JsonResponse({'error': 'Token expired'}, status=401)
                except jwt.InvalidTokenError:
                    return JsonResponse({'error': 'Invalid token'}, status=401)
