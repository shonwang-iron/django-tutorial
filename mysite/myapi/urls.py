from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.home, name='home'),
    path('employee/all', views.employee_all, name='employee_all'),
    path('employee/detail/<int:employee_id>', views.employee_detail, name='employee_detail')
]