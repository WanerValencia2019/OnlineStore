from django.urls import path

from . import views


app_name = 'billing_profiles'

urlpatterns = [
	path('create',views.Create.as_view(), name="create")
]