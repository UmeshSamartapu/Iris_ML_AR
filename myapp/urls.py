from django.urls import path, include
from . import views

urlpatterns = [
    # 1. ML Predictor Home (The form to enter Sepal/Petal data)
    path('', views.home, name='home'),

    # 2. AR Explorer Selection (The landing page to choose Mobile or Laptop)
    path('explore/', views.landing_page, name='landing'),

    # 3. Mobile AR View (Uses Google Model Viewer)
    path('mobile/', views.mobile_view, name='mobile_ar'),

    # 4. Laptop AR View (Uses AR.js + Hiro Marker)
    path('laptop_ar/', views.laptop_view, name='laptop_ar'),
]