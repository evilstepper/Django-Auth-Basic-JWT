from django.urls import path,include
from .views import Sign_Up, Sign_In, Me, Sign_Out


# Import other views as needed

# urlpatterns = [
#     path('sign-up', Sign_Up.as_view()),
#     path('sign-in', Sign_In.as_view()),
#     path('me', Me.as_view()),
#     path('sign-out', Sign_Out.as_view()),
#     # Add other authentication paths
# ]
urlpatterns = [
    path('auth/', include([
        path('sign-up', Sign_Up.as_view()),
        path('sign-in', Sign_In.as_view()),
        path('me', Me.as_view()),
        path('sign-out', Sign_Out.as_view()),
    ])),
]
