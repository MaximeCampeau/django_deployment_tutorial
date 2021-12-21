from django.urls import path
from basic_app import views

# * Template Tagging. This variable must match the application name and is mandatory for template tagging in Django.
app_name = "basic_app"

urlpatterns = [
  path('relative/', views.relative, name="relative"),
  path('other/', views.other, name="other")
]