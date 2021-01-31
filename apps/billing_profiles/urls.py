from django.urls import path

from . import views


app_name = 'billing_profiles'

urlpatterns = [
	path('',views.BillingProfilesList.as_view(), name="list"),
	path('create',views.Create.as_view(), name="create"),
	path('default',views.defaultBilling,name='default'),
    path('delete',views.deleteBilling,name='delete'),
]