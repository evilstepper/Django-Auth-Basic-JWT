
from rest_framework.response import Response
from users.serializers import UserSerializer

def signup_user(data):
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data
