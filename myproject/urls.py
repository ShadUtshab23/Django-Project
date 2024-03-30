from django.urls import path
from Login.views import CustomLoginView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),  # Define a URL pattern for the root path
    path('login/', CustomLoginView.as_view(), name='login'),  # Keep the URL pattern for login
]
