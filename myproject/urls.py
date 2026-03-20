from django.contrib import admin
from django.urls import path, include # Corrected import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')), # This tells Django to look into your app's urls.py
]